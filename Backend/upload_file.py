from flask import Blueprint, jsonify, request, current_app as app
import os
from werkzeug.utils import secure_filename
import mysql.connector
from datetime import datetime
import logging
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS

upload_blueprint = Blueprint('upload', __name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@upload_blueprint.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        if not allowed_file(file.filename):
            return jsonify({'error': 'File type not allowed'}), 400
        
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(file_path):
            return jsonify({'error': 'File already exists'}), 400
        
        # Save the file
        file.save(file_path)
        
        # Get file metadata
        file_size = os.path.getsize(file_path)
        content_type = file.content_type
        
        # Database connection using a context manager
        with mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "your_database")
        ) as connection:
            with connection.cursor() as cursor:
                # Insert file metadata into the Documents table
                insert_query = """
                INSERT INTO Documents (userId, fileName, filePath, fileSize, contentType, status, uploadDate, createdBy, createdDate, lastModifiedDate)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                current_time = datetime.now()
                values = (
                    1,  # Replace with actual userId
                    filename,
                    file_path,
                    file_size,
                    content_type,
                    'uploaded',
                    current_time,
                    1,  # Replace with actual createdBy userId
                    current_time,
                    current_time
                )
                
                cursor.execute(insert_query, values)
                connection.commit()
        
        return jsonify({'message': 'File successfully uploaded and recorded in database', 'file_path': file_path})
    except Exception as e:
        logging.error(f"Error uploading file: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500