import '../models/file_model.dart';

class FileService {
  Future<List<FileModel>> getFiles() async {
    // Simulate API call
    await Future.delayed(const Duration(seconds: 1));

    return [
      FileModel(
          name: 'FAQs.txt', uploadedBy: 'Kojo A.', lastModified: '07-18-2024', fileSize: '0.2 MB'),
      FileModel(
          name: 'Process.docx',
          uploadedBy: 'Kojo A.',
          lastModified: '07-19-2024',
          fileSize: '0.8 MB'),
      FileModel(
          name: 'Workflow.pdf',
          uploadedBy: 'Kojo A.',
          lastModified: '07-19-2024',
          fileSize: '0.4 MB'),
    ];
  }
}
