from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import logging

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configuration for file uploads
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
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