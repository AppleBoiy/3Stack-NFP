'use client';

import {useEffect, useState} from 'react';
import {listUsers} from '@/utils/api';

interface User {
    id: number;
    username: string;
}

export default function ListUsers() {
    const [users, setUsers] = useState<User[]>([]);

    useEffect(() => {
        listUsers().then(response => setUsers(response.data));
    }, []);

    return (
        <div>
            <ul>
                {users.map(user => (
                    <li key={user.id}>{user.username}</li>
                ))}
            </ul>
        </div>
    );
}
