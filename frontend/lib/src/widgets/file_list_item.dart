import 'package:flutter/material.dart';
import '../models/document.dart';

class FileListItem extends StatelessWidget {
  final Document file;

  const FileListItem({super.key, required this.file});

  @override
  Widget build(BuildContext context) {
    return ListTile(
      title: Text(file.fileName),
      subtitle: Text(file.fileSize),
      trailing: Text(file.uploadDate),
      onTap: () {
        // Handle file tap
      },
    );
  }
}
