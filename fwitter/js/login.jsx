import React from 'react';
import PropTypes from 'prop-types';
import { Redirect } from 'react-router-dom';

class Login extends React.Component {
  constructor(props) {
    super(props);
    this.state = { inputUsername: '', password: '', redirectToProfile: null };
    this.onSubmit = this.onSubmit.bind(this);
    this.onChangeUsername = this.onChangeUsername.bind(this);
    this.onChangePassword = this.onChangePassword.bind(this);
  }

  onChangePassword(event) {
    this.setState({
      password: event.target.value,
    });
  }

  onChangeUsername(event) {
    this.setState({
      inputUsername: event.target.value,
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
          inputUsername: data.username,
          redirectToProfile: true,
        });
      })
      .catch((error) => {
        if (error !== 401) {
          console.log(error);
        } else {
          this.setState({
            inputUsername: '',
            redirectToProfile: false,
          });
        }
      });
  }

  render() {
    const { redirectToProfile } = this.state;
    const { inputUsername } = this.state;
    const { password } = this.state;
    const profileUrl = `/users/${inputUsername}`;
    const { username } = this.props;
    const propsProfileUrl = `/users/${username}`;
    const { loggedIn } = this.props;
    return (
      <div>
        { loggedIn
            && <Redirect to={propsProfileUrl} />
        }
        { !redirectToProfile
            && (
            <form id="login" onSubmit={this.onSubmit}>
                Username:
              {' '}
              <input id="username" value={inputUsername} type="text" onChange={this.onChangeUsername} />
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

Login.propTypes = {
  loggedIn: PropTypes.bool.isRequired,
  username: PropTypes.string.isRequired,
};

  
export default Login;
