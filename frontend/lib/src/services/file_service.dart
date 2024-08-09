import 'package:http/http.dart' as http;
import 'package:file_picker/file_picker.dart';
import 'dart:convert';
import 'package:flutter/foundation.dart';
import '../models/document.dart';

class FileService {
  final String baseUrl = 'http://127.0.0.1:5005';

  Future<List<Document>> getFiles() async {
    try {
      final response = await http.get(Uri.parse('$baseUrl/files'));

      if (response.statusCode == 200) {
        final Map<String, dynamic> data = json.decode(response.body);
        final List<dynamic> filesData = data['files'];
        print('files: $filesData');
        return filesData.map((fileData) => Document.fromJson(fileData)).toList();
      } else {
        throw Exception('Failed to load files');
      }
    } catch (e) {
      throw Exception('Error fetching files: $e');
    }
  }

  Future<bool> uploadFile() async {
    FilePickerResult? result = await FilePicker.platform.pickFiles();

    if (result != null) {
      PlatformFile file = result.files.first;

      var request = http.MultipartRequest('POST', Uri.parse('$baseUrl/upload'));

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
          return true;
        } else {
          var responseBody = json.decode(response.body);
          String errorMessage = responseBody['error'] ?? 'Unknown error occurred';
          throw Exception(errorMessage);
        }
      } catch (e) {
        throw Exception('Error uploading file: $e');
      }
    }
    return false;
  }
}
