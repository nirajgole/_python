import React, { useEffect, useState } from 'react';
import { axiosInstance } from '../Axios';

export const ListItem = () => {
  const [items, setItems] = useState([]);

  useEffect(() => {
    const getUsers = async () => {
      const data = await axiosInstance
        .get('/users')
        .then(({ data }) => data)
        .catch(err => console.log(err));
        console.log(data)
      setItems(data);
    };

    getUsers();
    //   return () => {
    //     second
    //   }
  }, []);
  //to-do implement table with pagination with sticky header
  return (
    <div>
      {items.map(({ name,email }) => (
        <div key={email}>{name}</div>
      ))}
    </div>
  );
};
