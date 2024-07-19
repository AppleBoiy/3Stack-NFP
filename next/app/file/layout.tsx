import React from 'react';
import Link from 'next/link';
import '@/styles/navbar.css';

const FileLayout: React.FC<{ children: React.ReactNode }> = ({children}) => {
    return (
        <div>
            <nav className="navbar">
                <Link href="/">Home</Link> |
                <Link href="/file">Document</Link> |
                <Link href="/file/list">List files</Link> |
                <Link href="/file/upload">Upload</Link> |
            </nav>
            {children}
        </div>
    );
};

export default FileLayout;
