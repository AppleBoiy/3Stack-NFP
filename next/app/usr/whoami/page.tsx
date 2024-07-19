'use client';
import React, {useEffect, useState} from 'react';
import {getCurrentUserInfo} from '@/utils/api';

interface User {
    id: number;
    username: string;
}

export default function WhoAmI() {
    const [user, setUser] = useState<User | null>(null);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const token = localStorage.getItem('token');
        if (!token) {
            setIsLoading(false);
            return;
        }

        getCurrentUserInfo(token)
            .then(response => {
                setUser(response.data);
                setIsLoading(false);
            })
            .catch(error => {
                console.error(error);
                setIsLoading(false);
            });
    }, []);

    return (
        <div>
            {isLoading && <p>Loading...</p>}
            {!isLoading && !user && <p>Please log in to view this page.</p>}
            {user && (
                <div>
                    <p>ID: {user.id}</p>
                    <p>Username: {user.username}</p>
                </div>
            )}
        </div>
    );
}
