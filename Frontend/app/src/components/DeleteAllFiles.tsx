import React from 'react';

interface DeleteAllFilesProps {
    handleDeleteAllFiles: () => void;
}

const DeleteAllFiles: React.FC<DeleteAllFilesProps> = ({ handleDeleteAllFiles }) => (
    <button className="delete" onClick={handleDeleteAllFiles}>
        Delete All Files
    </button>
);

export default DeleteAllFiles;
