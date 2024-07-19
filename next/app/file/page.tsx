'use client';
import React from 'react';

import '@/styles/button.css';
import '@/styles/table.css';
import Markdown from "@/components/markdown";

const FILES_DOC = 'https://raw.githubusercontent.com/AppleBoiy/3Stack-NFP/main/docs/files.md'

const File: React.FC = () => {
    return <div>
        <Markdown url={FILES_DOC}/>
    </div>
};

export default File;