from flask import Blueprint, jsonify, current_app as app
import logging
from config.file_upload_config import DB_FILE
from model.document import Document
from repository.document_repository import DocumentRepository
from typing import List, Dict, Any

# Set up logging
logging.basicConfig(level=logging.DEBUG)

get_files_blueprint = Blueprint('files', __name__)

# Instantiate the repository
document_repository = DocumentRepository(DB_FILE)

@get_files_blueprint.route('/files', methods=['GET'])
def get_files():
    try:
        # Retrieve all documents from the repository
        documents: List[Document] = document_repository.get_all_documents()
        
        # Convert documents to a list of dictionaries
        document_list: List[Dict[str, Any]] = [doc.to_dict() for doc in documents]
        
        return jsonify({
            'message': 'Files retrieved successfully',
            'files': document_list
        }), 200

    except Exception as e:
        logging.error(f"Error retrieving files: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500