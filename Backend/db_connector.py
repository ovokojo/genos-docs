import sqlite3
import os
from dotenv import load_dotenv
from datetime import datetime
from config import DB_FILE

# Load environment variables
load_dotenv()

# Database file path
DB_FILE = os.getenv("DB_FILE", "db.sqlite")

def init_db():
    conn = create_db_connection()
    if conn:
        create_users_table_query = """
        CREATE TABLE IF NOT EXISTS Users (
            userId INTEGER PRIMARY KEY,
            organizationId INTEGER,
            role TEXT,
            firstName TEXT,
            lastName TEXT,
            email TEXT,
            status TEXT,
            lastLoginDate TEXT,
            createdBy INTEGER,
            createdDate TEXT,
            lastModifiedDate TEXT
        );
        """

        create_documents_table_query = """
        CREATE TABLE IF NOT EXISTS Documents (
            documentId INTEGER PRIMARY KEY,
            userId INTEGER,
            fileName TEXT,
            filePath TEXT,
            fileSize INTEGER,
            description TEXT,
            contentType TEXT,
            status TEXT,
            uploadDate TEXT,
            lastAccessDate TEXT,
            createdBy INTEGER,
            createdDate TEXT,
            lastModifiedDate TEXT,
            tags TEXT,
            version INTEGER,
            accessLevel TEXT,
            processingStatus TEXT,
            processingStartDate TEXT,
            processingEndDate TEXT,
            FOREIGN KEY (userId) REFERENCES Users(userId)
        );
        """
        # Add example data to test the schema
        add_example_user_data_query = """
        INSERT INTO Users (userId, organizationId, role, firstName, lastName, email, status, lastLoginDate, createdBy, createdDate, lastModifiedDate) 
        VALUES (1, 1, 'admin', 'John', 'Doe', 'john.doe@example.com', 'active', '2024-07-22 10:00:00', 1, '2024-07-22 09:00:00', '2024-07-22 09:00:00');
        """

        add_example_document_data_query = """
        INSERT INTO Documents (documentId, userId, fileName, filePath, fileSize, description, contentType, status, uploadDate, lastAccessDate, createdBy, createdDate, lastModifiedDate, tags, version, accessLevel, processingStatus, processingStartDate, processingEndDate) 
        VALUES (1, 1, 'example.txt', '/path/to/example.txt', 1234, 'An example text file.', 'txt', 'uploaded', '2024-07-22 09:00:00', '2024-07-22 09:15:00', 1, '2024-07-22 09:00:00', '2024-07-22 09:00:00', 'example, test', 1, 'public', 'not started', NULL, NULL);
        """

        # Execute each query
        execute_query(conn, create_users_table_query)
        execute_query(conn, create_documents_table_query)
        execute_query(conn, add_example_user_data_query)
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