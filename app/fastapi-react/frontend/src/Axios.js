import axios from 'axios';

export const axiosInstance = axios.create({
  // baseURL: `${process.env.REACT_APP_BACKEND_URL}`,
  baseURL: `http://localhost:8000/`,
  headers: {
    'Access-Control-Allow-Origin': '*',
     "Content-Type": "application/json",
  }
});
