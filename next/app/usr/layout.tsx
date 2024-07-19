import React from 'react';
import Link from 'next/link';
import '@/styles/navbar.css';

const UsrLayout: React.FC<{ children: React.ReactNode }> = ({children}) => {
    return (
        <div>
            <nav className="navbar">
                <Link href="/">Home</Link> |
                <Link href="/usr">Document</Link> |
                <Link href="/usr/list">Users</Link> |
                <Link href="/usr/login">Login</Link> |
                <Link href="/usr/register">Register</Link> |
                <Link href="/usr/whoami">Who Am I</Link> |
                <Link href="/usr/logout">Logout</Link>
            </nav>
            {children}
        </div>
    );
};

export default UsrLayout;
