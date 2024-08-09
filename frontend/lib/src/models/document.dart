class Document {
  final String documentId;
  final String fileName;
  final int fileSize;
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
      documentId: json['documentId'] as String,
      fileName: json['fileName'] as String,
      fileSize: json['fileSize'] as int,
      fileType: json['fileType'] as String,
      uploadDate: json['uploadDate'] as String,
    );
  }
}
