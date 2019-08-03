import React from 'react';
import { HashRouter, Link } from 'react-router-dom';
import '../static/css/header.css';

const Header = () => (
  <div className="header">
    Fwitter
    <Link to="/Logout">Logout</Link>
    </div>
);

export default Header;
