import 'package:flutter/material.dart';
import '../widgets/file_list_item.dart';
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

  @override
  void initState() {
    super.initState();
    _loadFiles();
  }

  void _loadFiles() async {
    final files = await _fileService.getFiles();
    setState(() {
      _files = files;
    });
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
      body: Column(
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              Padding(
                padding: const EdgeInsets.all(12.0),
                child: Text(
                  'Knowledge Base',
                  style: Theme.of(context).textTheme.bodyLarge,
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
            child: ListView.builder(
              itemCount: _filteredFiles.length,
              itemBuilder: (context, index) {
                return FileListItem(file: _filteredFiles[index]);
              },
            ),
          ),
        ],
      ),
    );
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
}
