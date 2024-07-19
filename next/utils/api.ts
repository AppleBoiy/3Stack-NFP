import axios from 'axios';

const BASE_URL = 'http://localhost:56733/';

export const api = axios.create({
    baseURL: BASE_URL,
});

// User API
export const listUsers = () => api.get('/users/');

export const registerUser = (username: string, password: string) =>
    api.post('/users/register', {username, password});

export const loginUser = (username: string, password: string) =>
    api.post('/users/login', {username, password});

export const logoutUser = () => {
    const token = localStorage.getItem('token');
    return api.post('/users/logout', null, {
        headers: {Authorization: `Bearer ${token}`},
    });
}

export const getCurrentUserInfo = (token: string) =>
    api.get('/users/whoami', {
        headers: {Authorization: `Bearer ${token}`},
    });

// File API
export const listFiles = () => api.get('/file/');

export const uploadFile = (file: File) => {
    const formData = new FormData();
    formData.append('file', file);

    return api.post('/file/upload', formData, {
        headers: {
            'Content-Type': 'multipart/form-data',
        },
    });
};

export const deleteFileById = (id: string) => api.delete(`/file/delete/${id}`);

export const getFileById = (id: string) => api.get(`/file/${id}`);

export const downloadFileById = (id: string) => {
    return api.get(`/file/download/${id}`, {
        responseType: 'blob', // Ensure response is treated as blob (file)
    });
};