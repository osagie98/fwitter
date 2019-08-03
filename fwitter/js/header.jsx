import React from 'react';
import { Link } from 'react-router-dom';
import '../static/css/header.css';

const Header = () => (
  <div className="header">
    Fwitter
    <Link id="logout" to="/Logout">Logout</Link>
  </div>
);

export default Header;
