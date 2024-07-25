class FileModel {
  final String name;
  final String uploadedBy;
  final String lastModified;
  final String fileSize;

  FileModel({
    required this.name,
    required this.uploadedBy,
    required this.lastModified,
    required this.fileSize,
  });

  factory FileModel.fromJson(Map<String, dynamic> json) {
    return FileModel(
      name: json['name'],
      uploadedBy: json['uploadedBy'],
      lastModified: json['lastModified'],
      fileSize: json['fileSize'],
    );
  }
}
