import React from 'react';
import { Redirect } from 'react-router-dom';
import fetch from 'isomorphic-fetch';

const Logout = () => {
  fetch('/api/v1/logout', {
    method: 'GET',
    credentials: 'same-origin',
    headers: { 'Content-Type': 'application/json' },
  })
    .then((response) => {
      if (!response.ok) throw Error(response.statusText);
      return response.json();
    })
    .catch(error => console.log(error));

  return (
    <Redirect to="/" />
  );
};

export default Logout;
