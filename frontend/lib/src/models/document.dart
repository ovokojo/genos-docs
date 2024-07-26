class Document {
  final int documentId;
  final String fileName;
  final int? userId;
  final String? filePath;
  final int? fileSize;
  final String? description;
  final String? contentType;
  final String? status;
  final DateTime? uploadDate;
  final DateTime? lastAccessDate;
  final int? createdBy;
  final DateTime createdDate;
  final DateTime? lastModifiedDate;
  final String? tags;
  final int? version;
  final String? accessLevel;
  final String? processingStatus;
  final DateTime? processingStartDate;
  final DateTime? processingEndDate;

  Document({
    required this.documentId,
    required this.fileName,
    this.userId,
    this.filePath,
    this.fileSize,
    this.description,
    this.contentType,
    this.status,
    this.uploadDate,
    this.lastAccessDate,
    this.createdBy,
    required this.createdDate,
    this.lastModifiedDate,
    this.tags,
    this.version,
    this.accessLevel,
    this.processingStatus,
    this.processingStartDate,
    this.processingEndDate,
  });

  factory Document.fromMap(Map<String, dynamic> map) {
    return Document(
      documentId: map['documentId'],
      fileName: map['fileName'],
      userId: map['userId'],
      filePath: map['filePath'],
      fileSize: map['fileSize'],
      description: map['description'],
      contentType: map['contentType'],
      status: map['status'],
      uploadDate: map['uploadDate'] != null ? DateTime.parse(map['uploadDate']) : null,
      lastAccessDate: map['lastAccessDate'] != null ? DateTime.parse(map['lastAccessDate']) : null,
      createdBy: map['createdBy'],
      createdDate: DateTime.parse(map['createdDate']),
      lastModifiedDate:
          map['lastModifiedDate'] != null ? DateTime.parse(map['lastModifiedDate']) : null,
      tags: map['tags'],
      version: map['version'],
      accessLevel: map['accessLevel'],
      processingStatus: map['processingStatus'],
      processingStartDate:
          map['processingStartDate'] != null ? DateTime.parse(map['processingStartDate']) : null,
      processingEndDate:
          map['processingEndDate'] != null ? DateTime.parse(map['processingEndDate']) : null,
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'documentId': documentId,
      'fileName': fileName,
      'userId': userId,
      'filePath': filePath,
      'fileSize': fileSize,
      'description': description,
      'contentType': contentType,
      'status': status,
      'uploadDate': uploadDate?.toIso8601String(),
      'lastAccessDate': lastAccessDate?.toIso8601String(),
      'createdBy': createdBy,
      'createdDate': createdDate?.toIso8601String(),
      'lastModifiedDate': lastModifiedDate?.toIso8601String(),
      'tags': tags,
      'version': version,
      'accessLevel': accessLevel,
      'processingStatus': processingStatus,
      'processingStartDate': processingStartDate?.toIso8601String(),
      'processingEndDate': processingEndDate?.toIso8601String(),
    };
  }
}
