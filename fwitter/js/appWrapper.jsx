import React from 'react';
import App from './app';
import { HashRouter } from 'react-router-dom';
import Header from './header';

const AppWrapper = () => (
  <HashRouter>
    <Header />
    <App />
  </HashRouter>
);

export default AppWrapper;
