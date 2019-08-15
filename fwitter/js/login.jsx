import React from 'react';
import { Redirect } from 'react-router-dom';

class Login extends React.Component {
  constructor(props) {
    super(props);
    this.state = { username: '', password: '', redirectToProfile: null };
    this.onSubmit = this.onSubmit.bind(this);
    this.onChangeUsername = this.onChangeUsername.bind(this);
    this.onChangePassword = this.onChangePassword.bind(this);
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
          redirectToProfile: true,
        });
      })
      .catch((error) => {
        if (error !== 401) {
          console.log(error);
        } else {
          this.setState({
            username: '',
            redirectToProfile: false,
          });
        }
      });
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
    // eslint-disable-next-line no-undef
    fetch('/api/v1/login', {
      method: 'POST',
      credentials: 'omit',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password }),
    })
      .then((response) => {
        if (!response.ok) throw response.status;
        return response.json();
      })
      .then((data) => {
        this.setState({
          username: data.username,
          redirectToProfile: true,
        });
      })
      .catch((error) => {
        if (error !== 401) {
          console.log(error);
        } else {
          this.setState({
            username: '',
            redirectToProfile: false,
          });
        }
      });
  }

  render() {
    const { redirectToProfile } = this.state;
    const { username } = this.state;
    const { password } = this.state;
    const profileUrl = `/users/${username}`;
    return (
      <div>
        { !redirectToProfile
            && (
            <form id="login" onSubmit={this.onSubmit}>
                Username:
              {' '}
              <input id="username" value={username} type="text" onChange={this.onChangeUsername} />
              <br />
                Password:
              {' '}
              <input id="password" value={password} type="text" onChange={this.onChangePassword} />
              <br />
              <input id="submit" type="submit" value="submit" />
            </form>
            )
            }
        { redirectToProfile
                && <Redirect to={profileUrl} />
            }
      </div>
    );
  }
}

export default Login;
