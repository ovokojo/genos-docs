import React from 'react';

interface FileListProps {
    files: string[];
}

const FileList: React.FC<FileListProps> = ({ files }) => (
    <>
        {files.length > 0 && (
            <>
                <h4>Uploaded Files</h4>
                <ul>
                    {files.map((file, index) => (
                        <li key={index}>
                            <a href={`http://localhost:5005/uploads/${file}`} download>
                                {file}
                            </a>
                        </li>
                    ))}
                </ul>
            </>
        )}
    </>
);

export default FileList;
