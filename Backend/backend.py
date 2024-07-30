from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import logging
from werkzeug.utils import secure_filename
from upload_file import upload_blueprint
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS, MAX_FILE_SIZE

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Register the Blueprint
app.register_blueprint(upload_blueprint)

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_FILE_SIZE'] = MAX_FILE_SIZE

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
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
        file.save(file_path)
        return jsonify({'message': 'File successfully uploaded', 'file_path': file_path})
    except Exception as e:
        logging.error(f"Error uploading file: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

@app.route('/files', methods=['GET'])
def list_files():
    try:
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        return jsonify({'files': files})
    except Exception as e:
        logging.error(f"Error listing files: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

@app.route('/uploads/<filename>', methods=['GET'])
def get_file(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    except Exception as e:
        logging.error(f"Error serving file {filename}: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

@app.route('/delete_all_files', methods=['DELETE'])
def delete_all_files():
    try:
        for filename in os.listdir(app.config['UPLOAD_FOLDER']):
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            if os.path.isfile(file_path):
                os.unlink(file_path)
        return jsonify({'message': 'All files successfully deleted'})
    except Exception as e:
        logging.error(f"Error deleting files: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5005)
