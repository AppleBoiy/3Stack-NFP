'use client';

import {useState} from 'react';
import {logoutUser} from '@/utils/api';
import '@/styles/button.css';

export default function Logout() {
    const [logoutSuccess, setLogoutSuccess] = useState(false);
    const [error, setError] = useState<string | null>(null);

    const handleLogout = async () => {
        try {
            await logoutUser();
            setLogoutSuccess(true);
        } catch (error) {
            setError(`${error}`)
        }
    };

    return (
        <div>
            <div>
                {logoutSuccess ? (
                    <p style={{color: 'green'}}>Logout successful!</p>
                ) : error ? (
                    <p style={{color: 'red'}}>{error}</p>
                ) : (
                    <button
                        className="button"
                        onClick={handleLogout}
                    >
                        Logout
                    </button>
                )}
            </div>
        </div>
    );
}
