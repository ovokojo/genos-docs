import React, { ChangeEvent } from 'react';

interface FileUploadProps {
    handleFileChange: (event: ChangeEvent<HTMLInputElement>) => void;
    handleFileUpload: () => void;
}

const FileUpload: React.FC<FileUploadProps> = ({ handleFileChange, handleFileUpload }) => (
    <>
        <input type="file" onChange={handleFileChange} />
        <br />
        <button className="upload" onClick={handleFileUpload}>
            Upload
        </button>
    </>
);

export default FileUpload;
