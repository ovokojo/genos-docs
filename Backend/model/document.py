class Document:
    def __init__(self, document_id, file_name, file_size, file_type, upload_date):
        self.document_id = document_id
        self.file_name = file_name
        self.file_size = file_size
        self.file_type = file_type
        self.upload_date = upload_date

    def to_dict(self):
        return {
            'documentId': self.document_id,
            'fileName': self.file_name,
            'fileSize': self.file_size,
            'fileType': self.file_type,
            'uploadDate': self.upload_date,
        }

    @classmethod
    def from_db_row(cls, row):
        return cls(
            document_id=row['documentId'],
            file_name=row['fileName'],
            file_size=row['fileSize'],
            file_type=row['fileType'],
            upload_date=row['uploadDate']
        )
