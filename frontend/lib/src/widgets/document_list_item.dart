import 'package:flutter/material.dart';
import '../models/document.dart';

class DocumentListItem extends StatelessWidget {
  final Document file;

  const DocumentListItem({super.key, required this.file});

  @override
  Widget build(BuildContext context) {
    return ListTile(
      title: Text(file.fileName),
      subtitle: Text('Uploaded by: ${file.createdBy}'),
      trailing: Text(file.fileSize.toString()),
      onTap: () {
        // Handle file tap
      },
    );
  }
}
