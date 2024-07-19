'use client';
import React, {useEffect, useState} from 'react';
import {deleteFileById, downloadFileById, listFiles} from '@/utils/api';

import '@/styles/button.css';
import '@/styles/table.css';


const FileList: React.FC = () => {
    const [loading, setLoading] = useState(true);
    const [files, setFiles] = useState<any[]>([]);

    const fetchFiles = async () => {
        try {
            const response = await listFiles();
            setFiles(response.data);
        } catch (error) {
            console.error('Error fetching files:', error);
        }
    };

    const handleDownload = async (id: string, filename: string) => {
        const isConfirmed = window.confirm('Are you sure you want to download this file?');
        try {
            if (!isConfirmed) {
                return;
            }
            const response = await downloadFileById(id);
            const url = window.URL.createObjectURL(new Blob([response.data]));
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', filename);
            document.body.appendChild(link);
            link.click();
            link.parentNode?.removeChild(link);
        } catch (error) {
            console.error('Error downloading file:', error);
        }
    };

    const handleDelete = async (id: string) => {
        const isConfirmed = window.confirm('Are you sure you want to delete this file?');
        if (!isConfirmed) {
            return; // Exit the function if the user cancels
        }

        try {
            await deleteFileById(id);
            await fetchFiles(); // Refresh the list after deletion
        } catch (error) {
            console.error('Error deleting file:', error);
        }
    };

    useEffect(() => {
        fetchFiles().then(() => setLoading(false));
    }, []);

    return (
        <div>
            {loading && <p>Loading...</p>}
            <table className="table-frame">
                <thead>
                <tr>
                    <th colSpan={2}>Files</th>
                    <th>Actions</th>
                </tr>
                </thead>
                <tbody>
                {files.map((file) => (
                    <tr key={file.id}>
                        <td>{file.id}</td>
                        <td>{file.filename}</td>
                        <td>
                            <button
                                onClick={() => handleDownload(file.id.toString(), file.filename)}
                                className="button"
                                style={{color: 'white', backgroundColor: 'green'}}
                            >
                                Download
                            </button>
                            &nbsp;
                            <button
                                onClick={() => handleDelete(file.id.toString())}
                                className="button"
                                style={{color: 'white', backgroundColor: 'red'}}
                            >
                                Delete
                            </button>
                        </td>
                    </tr>
                ))}
                </tbody>
            </table>
        </div>
    );
};

export default FileList;