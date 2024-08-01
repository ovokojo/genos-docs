from flask import Flask
from flask_cors import CORS
import os
import logging
from utils.database_util import init_db
from routes.upload_file import upload_blueprint
from routes.get_files import get_files_blueprint
from config.file_upload_config import UPLOAD_FOLDER, MAX_FILE_SIZE

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize the database
init_db()

# Register the Blueprint
app.register_blueprint(upload_blueprint)
app.register_blueprint(get_files_blueprint)

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_FILE_SIZE'] = MAX_FILE_SIZE

# Set up logging
logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    app.run(debug=True, port=5005)
