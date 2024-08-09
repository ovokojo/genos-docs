import 'package:flutter/material.dart';
import '../models/document.dart';
import '../services/file_service.dart';
import '../services/alert_service.dart';

class KnowledgeBaseScreen extends StatefulWidget {
  const KnowledgeBaseScreen({super.key});

  @override
  State<KnowledgeBaseScreen> createState() => _KnowledgeBaseScreenState();
}

class _KnowledgeBaseScreenState extends State<KnowledgeBaseScreen> {
  final FileService _fileService = FileService();
  List<Document> _files = [];
  String _searchQuery = '';
  bool _isUploading = false;
  bool _isLoading = false;

  @override
  void initState() {
    super.initState();
    _loadFiles();
  }

  Future<void> _loadFiles() async {
    setState(() {
      _isLoading = true;
    });
    try {
      final files = await _fileService.getFiles();
      setState(() {
        _files = files;
        _isLoading = false;
      });
    } catch (e) {
      setState(() {
        _isLoading = false;
      });
      if (!mounted) return;
      AlertService.showErrorDialog(context, 'Failed to load files: ${e.toString()}');
    }
  }

  void _filterFiles(String query) {
    setState(() {
      _searchQuery = query;
    });
  }

  List<Document> get _filteredFiles {
    return _files
        .where((file) => file.fileName.toLowerCase().contains(_searchQuery.toLowerCase()))
        .toList();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(40.0),
        child: Column(
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.start,
              children: [
                Padding(
                  padding: const EdgeInsets.all(12.0),
                  child: Text(
                    'Knowledge Base',
                    style: Theme.of(context).textTheme.headlineSmall,
                  ),
                )
              ],
            ),
            Padding(
              padding: const EdgeInsets.all(12.0),
              child: Row(
                children: [
                  Expanded(
                    child: TextField(
                      decoration: const InputDecoration(
                        hintText: 'Search',
                        prefixIcon: Icon(Icons.search),
                      ),
                      onChanged: _filterFiles,
                    ),
                  ),
                  const SizedBox(width: 8),
                  ElevatedButton.icon(
                    icon: const Icon(Icons.add),
                    label: const Text('Add Documents'),
                    onPressed: _isUploading ? null : _uploadFile,
                  ),
                  if (_isUploading)
                    const Padding(
                      padding: EdgeInsets.only(left: 8.0),
                      child: SizedBox(
                        width: 20,
                        height: 20,
                        child: CircularProgressIndicator(
                          strokeWidth: 2,
                        ),
                      ),
                    ),
                ],
              ),
            ),
            Expanded(
              child: _isLoading
                  ? const Center(child: CircularProgressIndicator())
                  : ListView.builder(
                      itemCount: _filteredFiles.length,
                      itemBuilder: (context, index) {
                        return _buildDocumentListItem(_filteredFiles[index]);
                      },
                    ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildDocumentListItem(Document document) {
    return Card(
      margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
      child: ListTile(
        leading: Icon(_getFileTypeIcon(document.fileType)),
        title: Text(document.fileName),
        subtitle:
            Text('${_formatFileSize(document.fileSize)} • ${document.fileType.toUpperCase()}'),
        trailing: Text(_formatDate(document.uploadDate)),
      ),
    );
  }

  IconData _getFileTypeIcon(String fileType) {
    switch (fileType.toLowerCase()) {
      case 'txt':
      case 'md':
        return Icons.description;
      case 'pdf':
        return Icons.picture_as_pdf;
      case 'doc':
      case 'docx':
        return Icons.article;
      default:
        return Icons.insert_drive_file;
    }
  }

  Future<void> _uploadFile() async {
    setState(() {
      _isUploading = true;
    });
    try {
      bool success = await _fileService.uploadFile();
      if (!mounted) return;
      setState(() {
        _isUploading = false;
      });
      if (success) {
        _loadFiles();
        AlertService.showSuccessSnackbar(context, 'File uploaded successfully');
      }
    } catch (e) {
      if (!mounted) return;
      setState(() {
        _isUploading = false;
      });
      AlertService.showErrorDialog(context, e.toString());
    }
  }

  String _formatFileSize(int sizeInBytes) {
    if (sizeInBytes < 1024) return '$sizeInBytes B';
    if (sizeInBytes < 1024 * 1024) return '${(sizeInBytes / 1024).toStringAsFixed(1)} KB';
    return '${(sizeInBytes / (1024 * 1024)).toStringAsFixed(1)} MB';
  }

  String _formatDate(String isoDate) {
    final date = DateTime.parse(isoDate);
    return '${date.year}-${date.month.toString().padLeft(2, '0')}-${date.day.toString().padLeft(2, '0')}';
  }
}
