import React from 'react';
import { HashRouter } from 'react-router-dom';
import App from './app';
import Header from './header';

const AppWrapper = () => (
  <HashRouter>
    <Header />
    <App />
  </HashRouter>
);

export default AppWrapper;
