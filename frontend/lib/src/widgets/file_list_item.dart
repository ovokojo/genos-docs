import 'package:flutter/material.dart';
import '../models/file_model.dart';

class FileListItem extends StatelessWidget {
  final FileModel file;

  const FileListItem({super.key, required this.file});

  @override
  Widget build(BuildContext context) {
    return ListTile(
      title: Text(file.name),
      subtitle: Text('Uploaded by: ${file.uploadedBy}'),
      trailing: Text(file.fileSize),
      onTap: () {
        // Handle file tap
      },
    );
  }
}
