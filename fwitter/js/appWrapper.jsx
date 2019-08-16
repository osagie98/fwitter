import React from 'react';
import { HashRouter } from 'react-router-dom';
import App from './app';
import Header from './header';

class AppWrapper extends React.Component {
  constructor(props) {
    super(props);
    this.state = {loggedIn: null};
  }

  render() {
    return (
      <HashRouter>
        <Header />
        <App />
      </HashRouter>
    );
  }
}

export default AppWrapper;
