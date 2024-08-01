import sqlite3
import os
from dotenv import load_dotenv
from datetime import datetime
from config.file_upload_config import DB_FILE

# Load environment variables
load_dotenv()

# Database file path
DB_FILE = os.getenv("DB_FILE", "db.sqlite")

def init_db():
    conn = create_db_connection()
    if conn:
        create_documents_table_query = """
        CREATE TABLE IF NOT EXISTS Documents (
            documentId TEXT PRIMARY KEY,
            fileName TEXT,
            fileSize INTEGER,
            fileType TEXT,
            uploadDate TEXT,
        );
        """
        # Add example data to test the schema
        add_example_document_data_query = """
        INSERT INTO Documents (documentId, userId, fileName, fileSize, fileType, status, uploadDate) VALUES
        ('af2d8ee5-962d-416c-ab8d-a2c0604cd4c8', 'd9f3548c-abb5-4c2e-b896-3a929dc49edc.txt', 1024000, 'txt', '2024-07-15'),
        ('9db4745d-64db-45fe-81dd-fe4b2309f814', '60bb3f86-20bf-4e1d-a128-63c766381d00.txt', 2048000, 'txt', '2024-07-16'),
        ('deb711a8-a2f9-45fa-96a2-97fda9df2881', '4b59f797-850e-4e76-8743-07aaf9ed5ac2.txt', 512000, 'text', '2024-07-17');
        """
        # Execute each query
        execute_query(conn, create_documents_table_query)
        execute_query(conn, add_example_document_data_query)

        conn.close()
        print("Database initialized successfully")
    else:
        print("Failed to initialize database")

def create_db_connection():
    """Create a database connection to the SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
        print(f"SQLite Database connection to '{DB_FILE}' successful")
    except sqlite3.Error as e:
        print(f"Error: '{e}'")
    return conn

def execute_query(connection, query):
    """Execute a query"""
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except sqlite3.Error as e:
        print(f"Error: '{e}'")

def print_table_contents(table_name):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Get column names
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [column[1] for column in cursor.fetchall()]
        
        # Fetch all rows
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        
        # Print column names
        print("\n", " | ".join(columns))
        print("-" * (len(" | ".join(columns)) + 5))
        
        # Print rows
        for row in rows:
            print(" | ".join(str(item) for item in row))
        
        print(f"\nTotal rows: {len(rows)}")
        
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()