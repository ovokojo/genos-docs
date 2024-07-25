import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

############################################################################################################
# Steps to run this script:
# Install mysql server into syatem and add sql bin path to environment variables and test installation by running 'mysql' in cmd    
# Do not forget to start sql server before running this script or else it gives connection error
# Install mysql in your system and create a database using mysql workbench or cmd and chage the details of db in the script
############################################################################################################

load_dotenv()


# Function to connect to a specific database
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print(f"MySQL Database connection to '{db_name}' successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as err:
        print(f"Error: '{err}'")


# Database information
host = os.getenv("DB_HOST") # Change this to your MySQL host
user = os.getenv("DB_USER") # Change this to your MySQL user
password = os.getenv("DB_PASSWORD") # Change this to your MySQL password
database = os.getenv("DB_NAME") # Change this to your MySQL database


print(host, user, password, database)
# Connect to the newly created database
db_connection = create_db_connection(host, user, password, database)


# Create Users table
create_users_table_query = """
CREATE TABLE IF NOT EXISTS Users (
    userId INT PRIMARY KEY,                     -- Primary key for the Users table
    organizationId INT,                         -- Foreign key to link users to organizations
    role VARCHAR(50),                           -- Role of the user (e.g., admin, editor, viewer)
    firstName VARCHAR(100),                     -- User's first name
    lastName VARCHAR(100),                      -- User's last name
    email VARCHAR(100),                         -- User's email address
    status VARCHAR(50),                         -- Status of the user (e.g., active, inactive)
    lastLoginDate DATETIME,                     -- Last login date of the user
    createdBy INT,                              -- ID of the user who created this record
    createdDate DATETIME,                       -- Date when the user record was created
    lastModifiedDate DATETIME                   -- Date when the user record was last modified
);
"""

# Create Documents table
create_documents_table_query = """
CREATE TABLE IF NOT EXISTS Documents (
    documentId INT PRIMARY KEY,                 -- Primary key for the Documents table
    userId INT,                                 -- Foreign key to link documents to users
    fileName VARCHAR(255),                      -- Name of the file
    filePath VARCHAR(255),                      -- Path where the file is stored
    fileSize INT,                               -- Size of the file in bytes
    description TEXT,                           -- Description of the document
    contentType VARCHAR(50),                    -- Content type of the document (e.g., txt, pdf)
    status VARCHAR(50),                         -- Status of the document (e.g., uploaded, processed)
    uploadDate DATETIME,                        -- Date when the document was uploaded
    lastAccessDate DATETIME,                    -- Date when the document was last accessed
    createdBy INT,                              -- ID of the user who created this document
    createdDate DATETIME,                       -- Date when the document record was created
    lastModifiedDate DATETIME,                  -- Date when the document record was last modified
    tags VARCHAR(255),                          -- Tags or categories for the document
    version INT,                                -- Version number of the document
    accessLevel VARCHAR(50),                    -- Access level for the document
    processingStatus VARCHAR(50),               -- Processing status of the document
    processingStartDate DATETIME,               -- Date when processing started
    processingEndDate DATETIME                  -- Date when processing ended
);
"""

# Add foreign key constraint to Documents table
add_constraints_and_indexes_query = """
ALTER TABLE Documents 
ADD CONSTRAINT FK_UserDocument 
FOREIGN KEY (userId) REFERENCES Users(userId);
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

# Execute each query separately and close the cursor after each execution
execute_query(db_connection, create_users_table_query)
execute_query(db_connection, create_documents_table_query)
execute_query(db_connection, add_constraints_and_indexes_query)
execute_query(db_connection, add_example_user_data_query)
execute_query(db_connection, add_example_document_data_query)

# Close the connection
db_connection.close()
