from flask import Blueprint, jsonify, request, current_app as app
import os
import sqlite3
from werkzeug.utils import secure_filename
from datetime import datetime
import logging
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS, DB_FILE
from db_connector import print_table_contents

upload_blueprint = Blueprint('upload', __name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def get_file_extension(filename):
    return os.path.splitext(filename)[1][1:].lower()

def allowed_file(filename):
    return get_file_extension(filename) in ALLOWED_EXTENSIONS

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
        file_extension = get_file_extension(filename)
        
        # Database connection using a context manager
        with sqlite3.connect(DB_FILE) as connection:
            cursor = connection.cursor()
            # Insert file metadata into the Documents table
            insert_query = """
            INSERT INTO Documents (userId, fileName, filePath, fileSize, contentType, status, uploadDate, createdBy, createdDate, lastModifiedDate)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            current_time = datetime.now().isoformat()
            user_id = 1  # Replace with actual userId
            values = (
                user_id,
                filename,
                file_path,
                file_size,
                file_extension,
                'uploaded',
                current_time,
                user_id,  # Replace with actual createdBy userId if different
                current_time,
                current_time
            )
            
            cursor.execute(insert_query, values)
            document_id = cursor.lastrowid  # Get the ID of the inserted row
            connection.commit()

            # Fetch the inserted record
            cursor.execute("SELECT * FROM Documents WHERE documentId = ?", (document_id,))
            document = cursor.fetchone()

            # Get column names
            column_names = [description[0] for description in cursor.description]

            # Create a dictionary from the fetched data
            document_dict = dict(zip(column_names, document))

        return jsonify({
            'message': 'File successfully uploaded and recorded in database',
            'document': {
                'documentId': document_dict['documentId'],
                'fileName': document_dict['fileName'],
                'userId': document_dict['userId'],
                'filePath': document_dict['filePath'],
                'fileSize': document_dict['fileSize'],
                'contentType': document_dict['contentType'],
                'status': document_dict['status'],
                'uploadDate': document_dict['uploadDate'],
                'lastAccessDate': document_dict['lastAccessDate'],
                'createdBy': document_dict['createdBy'],
                'createdDate': document_dict['createdDate'],
                'lastModifiedDate': document_dict['lastModifiedDate'],
                'tags': document_dict['tags'],
                'version': document_dict['version'],
                'accessLevel': document_dict['accessLevel'],
                'processingStatus': document_dict['processingStatus'],
                'processingStartDate': document_dict['processingStartDate'],
                'processingEndDate': document_dict['processingEndDate']
            }
        }), 200

    except Exception as e:
        logging.error(f"Error uploading file: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500