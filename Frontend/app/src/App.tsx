import React, { useState, useEffect, ChangeEvent } from 'react';
import axios from 'axios';
import './App.css';
import FileList from './components/FileList';
import FileUpload from './components/FileUpload';
import Message from './components/Message';
import DeleteAllFiles from './components/DeleteAllFiles';

function App() {
  const [selectedFile, setSelectedFile] = useState<File | undefined>(undefined);
  const [message, setMessage] = useState('');
  const [files, setFiles] = useState<string[]>([]);

  useEffect(() => {
    fetchFiles();
  }, []);

  const fetchFiles = async () => {
    try {
      const response = await axios.get('http://localhost:5005/files');
      setFiles(response.data.files);
    } catch (error) {
      console.error('Error fetching files:', error);
    }
  };

  const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    setSelectedFile(file);
  };

  const handleFileUpload = async () => {
    if (!selectedFile) {
      setMessage('Please select a file to upload.');
      return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await axios.post('http://localhost:5005/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      setMessage(response.data.message);
      fetchFiles(); // Refresh the list of files after a successful upload
    } catch (error) {
      console.error('Error uploading file:', error);
      setMessage('Error uploading file');
    }
  };

  const handleDeleteAllFiles = async () => {
    try {
      const response = await axios.delete('http://localhost:5005/delete_all_files');
      setMessage(response.data.message);
      fetchFiles(); // Refresh the list of files after deletion
    } catch (error) {
      console.error('Error deleting files:', error);
      setMessage('Error deleting files');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Genos Docs</h1>
        <h3>Upload a file to get started</h3>
        <FileUpload handleFileChange={handleFileChange} handleFileUpload={handleFileUpload} />
        <br />
        <DeleteAllFiles handleDeleteAllFiles={handleDeleteAllFiles} />
        <br />
        <Message message={message} />
        <FileList files={files} />
      </header>
    </div>
  );
}

export default App;
