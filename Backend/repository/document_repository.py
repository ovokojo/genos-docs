import sqlite3
from model.document import Document

class DocumentRepository:
    def __init__(self, db_file):
        self.db_file = db_file
        self._initialize_database()

    def _initialize_database(self):
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            create_table_query = """
            CREATE TABLE IF NOT EXISTS Documents (
                documentId TEXT PRIMARY KEY,
                fileName TEXT NOT NULL,
                fileSize INTEGER NOT NULL,
                fileType TEXT NOT NULL,
                uploadDate TEXT NOT NULL
            )
            """
            cursor.execute(create_table_query)
            connection.commit()

    def insert_document(self, document):
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            insert_query = """
            INSERT INTO Documents (documentId, fileName, fileSize, fileType, uploadDate)
            VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(insert_query, (
                document.document_id,
                document.file_name,
                document.file_size,
                document.file_type,
                document.upload_date
            ))
            connection.commit()

    def get_document_by_id(self, document_id):
        with sqlite3.connect(self.db_file) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Documents WHERE documentId = ?", (document_id,))
            row = cursor.fetchone()
            return Document.from_db_row(row) if row else None

    def document_exists(self, filename):
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT 1 FROM Documents WHERE fileName = ?", (filename,))
            return cursor.fetchone() is not None
