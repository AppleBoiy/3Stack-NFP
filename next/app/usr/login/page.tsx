'use client';

import {useState} from 'react';
import {loginUser} from '@/utils/api';
import {useRouter} from 'next/navigation';


export default function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');
    const router = useRouter();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            const response = await loginUser(username, password);
            localStorage.setItem('token', response.data.access_token);
            setMessage('Login successful!');
            setTimeout(() => {
                router.push('/usr/whoami');
            }, 2000);
        } catch (error: any) {
            setMessage('Invalid credentials');
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required
                />
                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
                <button
                    type="submit"
                    className="button"
                >Login
                </button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
}
