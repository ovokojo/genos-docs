from repository.document_repository import DocumentRepository
from model.document import Document
import datetime

def test_get_all_documents():
    print('getting all documents..')
    # Create a test database file
    test_db_file = "test_documents.db"
    
    # Initialize the repository
    repo = DocumentRepository(test_db_file)
    
    # Insert some test documents
    test_documents: list[Document] = [
        Document("doc1", "file1.txt", 100, "txt", datetime.datetime.now().isoformat()),
        Document("doc2", "file2.pdf", 200, "pdf", datetime.datetime.now().isoformat()),
        Document("doc3", "file3.docx", 300, "docx", datetime.datetime.now().isoformat())
    ]
    
    for doc in test_documents:
        repo.insert_document(doc)
    
    # Retrieve all documents
    all_documents: list[Document] = repo.get_all_documents()
    
    # Print the results
    print("All documents:")
    for doc in all_documents:
        print(f"ID: {doc.document_id}, Name: {doc.file_name}, Size: {doc.file_size}, Type: {doc.file_type}, Upload Date: {doc.upload_date}")

if __name__ == "__main__":
    test_get_all_documents()