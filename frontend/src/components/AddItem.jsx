import {
  Button,
  Container,
  Grid,
  Paper,
  Stack,
  TextField
} from '@mui/material';
import React, { useState } from 'react';
import { axiosInstance } from '../Axios';

export const AddItem = () => {
  const [userName, setUserName] = useState('');
  const [userEmail, setUserEmail] = useState('');
  const [userPassword, setUserPassword] = useState('');

  const addUser = async () => {
    await axiosInstance
      .post('/', { name: userName, email: userEmail, password: userPassword })
      .then(res => alert(res.data));
  };

  const onHandleChange = ({ target: { value } }) => {
    setUserName(value);
  };
  const onHandleEmailChange = ({ target: { value } }) => {
    setUserEmail(value);
  };
  const onHandlePasswordChange = ({ target: { value } }) => {
    setUserPassword(value);
  };
  return (
    <div>
      <TextField
        id='userName'
        label='Name'
        variant='outlined'
        onChange={onHandleChange}
        value={userName}
        // onChangeCapture={onHandleChange}
      />
      <TextField
        id='outlined-basic'
        label='Email'
        variant='outlined'
        onChange={onHandleEmailChange}
        value={userEmail}
      />
      <TextField
        id='outlined-basic'
        label='Password'
        variant='outlined'
        onChange={onHandlePasswordChange}
        value={userPassword}
      />
      <Button variant='contained' onClick={addUser}>
        Contained
      </Button>
    </div>
  );
};
