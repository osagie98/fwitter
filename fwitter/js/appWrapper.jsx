import React from 'react';
import { HashRouter } from 'react-router-dom';
import App from './app';
import Header from './header';

class AppWrapper extends React.Component {
  constructor(props) {
    super(props);
    this.state = { loggedIn: false, username: '' };
  }

  componentDidMount() {
    // eslint-disable-next-line no-undef
    fetch('/api/v1/check_login', { credentials: 'omit' })
      .then((response) => {
        if (!response.ok) throw response.status;
        return response.json();
      })
      .then((data) => {
        this.setState({
          username: data.username,
          loggedIn: true,
        });
      })
      .catch((error) => {
        if (error !== 401) {
          console.log(error);
        } else {
          this.setState({
            username: '',
            loggedIn: false,
          });
        }
      });
  }

  render() {
    const { loggedIn } = this.state;
    const { username } = this.state;
    return (
      <HashRouter>
        <Header loggedIn={loggedIn} username={username} />
        <App loggedIn={loggedIn} username={username} />
      </HashRouter>
    );
  }
}

export default AppWrapper;
