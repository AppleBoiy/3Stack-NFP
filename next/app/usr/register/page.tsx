'use client';

import {useState} from 'react';
import {registerUser} from '@/utils/api';
import {useRouter} from 'next/navigation';
import '@/styles/button.css';

export default function Register() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');
    const router = useRouter();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            const response = await registerUser(username, password);
            setMessage(response.data.message);
            setTimeout(() => {
                router.push('/usr');
            }, 2000);
        } catch (error: any) {
            setMessage(error.response.data.message);
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
                >Register
                </button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
}
