import 'package:flutter/material.dart';
import 'package:file_picker/file_picker.dart';
import 'package:http/http.dart' as http;
import 'package:flutter/foundation.dart' show kIsWeb;
import 'dart:convert';
import '../widgets/document_list_item.dart';
import '../models/document.dart';
import '../services/file_service.dart';

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
    final files = await _fileService.getDocuments();
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

  Future<bool> _uploadFile() async {
    FilePickerResult? result = await FilePicker.platform.pickFiles();

    if (result != null) {
      PlatformFile file = result.files.first;

      var request = http.MultipartRequest('POST', Uri.parse('http://127.0.0.1:5005/upload'));

      if (kIsWeb) {
        request.files.add(http.MultipartFile.fromBytes(
          'file',
          file.bytes!,
          filename: file.name,
        ));
      } else {
        request.files.add(await http.MultipartFile.fromPath(
          'file',
          file.path!,
          filename: file.name,
        ));
      }

      try {
        var streamedResponse = await request.send();
        var response = await http.Response.fromStream(streamedResponse);

        if (response.statusCode == 200) {
          // Reload the file list
          _loadFiles();
          return true;
        } else {
          // Parse the error message from the response
          var responseBody = json.decode(response.body);
          String errorMessage = responseBody['error'] ?? 'Unknown error occurred';
          _showErrorDialog(errorMessage);
          return false;
        }
      } catch (e) {
        _showErrorDialog('Error uploading file: $e');
        return false;
      }
    }
    return false;
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
                  onPressed: _isUploading
                      ? null
                      : () async {
                          setState(() {
                            _isUploading = true;
                          });
                          bool? success = await _uploadFile();
                          setState(() {
                            _isUploading = false;
                          });
                          if (success == true) {
                            _showSuccessSnackbar();
                          }
                        },
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
                return DocumentListItem(file: _filteredFiles[index]);
              },
            ),
          ),
        ],
      ),
    );
  }

  void _showErrorDialog(String errorMessage) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: const Text('Upload Error'),
          content: Text(errorMessage),
          actions: <Widget>[
            TextButton(
              child: const Text('OK'),
              onPressed: () {
                Navigator.of(context).pop();
              },
            ),
          ],
        );
      },
    );
  }

  void _showSuccessSnackbar() {
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(
        content: Row(
          children: [
            Icon(Icons.check_circle, color: Colors.white),
            SizedBox(width: 8),
            Text('File uploaded successfully!'),
          ],
        ),
        backgroundColor: Colors.green,
        behavior: SnackBarBehavior.floating,
        margin: EdgeInsets.all(8),
        duration: Duration(seconds: 3),
      ),
    );
  }
}
