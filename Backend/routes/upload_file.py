from flask import Blueprint, jsonify, request, current_app as app
from werkzeug.datastructures.file_storage import FileStorage
from werkzeug.utils import secure_filename
from datetime import datetime
import uuid
import os
import logging
from config.file_upload_config import DB_FILE
from utils.file_util import allowed_file, get_file_extension
from model.document import Document
from repository.document_repository import DocumentRepository
from typing import Any

# Set up logging
logging.basicConfig(level=logging.DEBUG)

upload_blueprint = Blueprint('upload', __name__)

# Instantiate the repository
document_repository = DocumentRepository(DB_FILE)

@upload_blueprint.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        file: FileStorage = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        if not allowed_file(file.filename):
            return jsonify({'error': 'File type not allowed'}), 400

        filename: str = secure_filename(file.filename)
        file_path: str = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if document_repository.document_exists(filename):
            return jsonify({'error': 'File already exists'}), 400
        file.save(file_path)

        file_size: int = os.path.getsize(file_path)
        file_type: str = get_file_extension(filename)
        upload_date: str = datetime.now().isoformat()
        document_id = str(uuid.uuid4())

        document = Document(document_id, filename, file_size, file_type, upload_date)
        document_repository.insert_document(document)
        document_data: dict[str, Any] = document.to_dict()
        print(document_data)
        return jsonify({
            'message': 'File successfully uploaded and recorded in database',
            'document': document_data
        }), 200

    except Exception as e:
        logging.error(f"Error uploading file: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500
