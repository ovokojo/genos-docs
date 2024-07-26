import '../models/document.dart';

class FileService {
  Future<List<Document>> getDocuments() async {
    // Simulate API call
    await Future.delayed(const Duration(seconds: 1));

    return [
      Document(
          documentId: 1,
          fileName: 'FAQs.txt',
          createdBy: 'Kojo A.',
          lastModifiedDate: DateTime(2024, 7, 20),
          fileSize: 2000),
      Document(
          documentId: 2,
          fileName: 'Process.docx',
          createdBy: 'Kojo A.',
          lastModifiedDate: DateTime(2024, 7, 20),
          fileSize: 8000),
      Document(
          documentId: 3,
          fileName: 'Workflow.pdf',
          createdBy: 'Kojo A.',
          lastModifiedDate: DateTime(2024, 7, 20),
          fileSize: 4000),
    ];
  }
}
