'use client';
import {usePathname} from 'next/navigation';

export default function PageHeader() {
    const currentPath = usePathname();

    return (
        <header>
            <p>You are here: {currentPath}</p>
        </header>
    );
}