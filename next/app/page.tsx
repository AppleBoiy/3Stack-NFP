'use client';
import Link from 'next/link';
import '@/styles/navbar.css';
import React from "react";
import Markdown from "@/components/markdown";

const READMEURL = 'https://raw.githubusercontent.com/AppleBoiy/3Stack-NFP/main/readme.md'


export default function Home() {

    return (
        <div>
            <nav className='navbar'>
                <Link href="/">Home</Link> |
                <Link href="/usr">Users</Link> |
                <Link href="/file">File</Link>
            </nav>
            <Markdown url={READMEURL}/>

        </div>
    );
}