import os

# DB configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, 'db.sqlite')

# File upload configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'md'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 16MB max file size