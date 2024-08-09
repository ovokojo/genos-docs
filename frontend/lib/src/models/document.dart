class Document {
  final String documentId;
  final String fileName;
  final String fileSize;
  final String fileType;
  final String uploadDate;

  Document({
    required this.documentId,
    required this.fileName,
    required this.fileSize,
    required this.fileType,
    required this.uploadDate,
  });

  factory Document.fromJson(Map<String, dynamic> json) {
    return Document(
      documentId: json['document_id'],
      fileName: json['file_name'],
      fileSize: json['file_size'],
      fileType: json['file_type'],
      uploadDate: json['upload_date'],
    );
  }
}
