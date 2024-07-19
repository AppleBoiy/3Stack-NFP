'use client';
import React, {useState} from 'react';
import {uploadFile} from '@/utils/api';

export default function FileUploadPage() {
    const [selectedFile, setSelectedFile] = useState<File | null>(null);
    const [uploadError, setUploadError] = useState<string | null>(null);
    const [uploadSuccess, setUploadSuccess] = useState<string | null>(null);

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files) {
            setSelectedFile(event.target.files[0]);
        }
    };

    const handleFileUpload = async () => {
        if (selectedFile) {
            try {
                await uploadFile(selectedFile);
                setUploadSuccess('File uploaded successfully');
                setSelectedFile(null);
                setUploadError(null);
            } catch (error) {
                console.error('Error uploading file:', error);
                setUploadError('Failed to upload file');
                setUploadSuccess(null);
            }
        } else {
            setUploadError('No file selected');
        }
    };

    return (
        <div>
            <input type="file" onChange={handleFileChange}/>
            <button
                onClick={handleFileUpload}
                style={{
                    color: 'white',
                    backgroundColor: '#007bff'
                }}>
                Upload
            </button>
            {uploadError && <p style={{color: 'red'}}>{uploadError}</p>}
            {uploadSuccess && <p style={{color: 'green'}}>{uploadSuccess}</p>}
        </div>
    );
}
