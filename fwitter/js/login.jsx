import React from 'react';
import { Redirect } from 'react-router-dom';
import fetch from 'isomorphic-fetch';

class Login extends React.Component {
  constructor(props) {
    super(props);
    this.state = { username: '', password: '', redirect: false };
    this.onSubmit = this.onSubmit.bind(this);
    this.onChangeUsername = this.onChangeUsername.bind(this);
    this.onChangePassword = this.onChangePassword.bind(this);
  }

  componentDidMount() {
    // TODO make api call to check if user is logged in
    fetch('/api/v1/checkLogin', { credentials: 'omit' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        console.log(response);
        return response.json();
      })
      .catch(error => console.log(error));
  }

  onChangePassword(event) {
    this.setState({
      password: event.target.value,
    });
  }

  onChangeUsername(event) {
    this.setState({
      username: event.target.value,
    });
  }

  onSubmit() {
    const { username } = this.state;
    const { password } = this.state;
    fetch('/api/v1/login', {
      method: 'POST',
      credentials: 'same-origin',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password }),
    })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then(() => {
        this.setState({
          redirect: true,
        });
      })
      .catch(error => console.log(error));
  }

  render() {
    const { redirect } = this.state;
    return (
      <div>
        { !redirect
            && (
            <form onSubmit={this.onSubmit}>
              <p>This is the login page</p>
              <br />
                Username:
              {' '}
              <input type="text" onChange={this.onChangeUsername} />
              <br />
                Password:
              {' '}
              <input type="text" onChange={this.onChangePassword} />
              <br />
              <input type="submit" />
            </form>
            )
            }
        { redirect
                && <Redirect to="/" />
            }
      </div>
    );
  }
}

export default Login;
