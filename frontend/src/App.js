import { useEffect, useState } from 'react';
import { axiosInstance } from './Axios';
import Button from '@mui/material/Button';
import { Box, Container } from '@mui/material';
import { Stack } from '@mui/system';
import { BoxWrapper } from './UiComponents';

const App = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const getUsers = async () => {
      const data = await axiosInstance.get('/users').then(res => res.data);
      setUsers(data);
      console.log(data);
    };
    getUsers();

    return () => {};
  }, []);

  return (
    <Container maxWidth='100%'>
      {/* <Stack direction={'row'}> */}
        <BoxWrapper
        >
          <>
          <span>UserList</span>
          {users.map(({ name, email }) => (
            <div key={email}>{name}</div>
          ))}
          </>
          <Button variant='contained'>Contained</Button>
        </BoxWrapper>
      {/* </Stack> */}
    </Container>
  );
};

export default App;
