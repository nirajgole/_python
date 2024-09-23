import { useEffect, useState } from 'react';
import { axiosInstance } from './Axios';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Unstable_Grid2';
import { Stack } from '@mui/system';
import { BoxWrapper } from './UiComponents';
import { Box, Container, Paper } from '@mui/material';
import { ListItem } from './components/ListItem';
import { AddItem } from './components/AddItem';

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
    <Container maxWidth='100%' fluid>
      <Grid container spacing={3}>
        <Grid xs>
          <Paper variant='outlined' square>
            <span>Add User</span>
            <AddItem/>
          </Paper>
        </Grid>
        <Grid xs>
          <Paper variant='outlined' square>
            <span>User List</span>
            <ListItem/>
          </Paper>
        </Grid>
      </Grid>
    </Container>
  );
};

export default App;
