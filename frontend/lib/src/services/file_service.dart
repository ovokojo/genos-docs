import '../models/document.dart';

class FileService {
  Future<List<Document>> getDocuments() async {
    // Simulate API call
    await Future.delayed(const Duration(seconds: 1));

    return [
      Document(
          documentId: 1, fileName: 'FAQs.txt', createdDate: DateTime(2024, 7, 20), fileSize: 2000),
      Document(
          documentId: 2,
          fileName: 'Process.docx',
          createdDate: DateTime(2024, 7, 20),
          fileSize: 8000),
      Document(
          documentId: 3,
          fileName: 'Workflow.pdf',
          createdDate: DateTime(2024, 7, 20),
          fileSize: 4000),
    ];
  }
}
