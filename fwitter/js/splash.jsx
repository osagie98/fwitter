import React from 'react';
import { Redirect, Link } from 'react-router-dom';

class SplashPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = { redirectToProfile: false, username: '' };
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
        }
      });
  }

  render() {
    const { redirectToProfile } = this.state;
    const { username } = this.state;
    const profileUrl = `/users/${username}`;
    return (
      <div className="login-or-redirect">
        { redirectToProfile
                && <Redirect to={profileUrl} />
                }
        { !redirectToProfile
                && (
                <div className="create-account-or-login">
                  <Link id="create" to="/create">Create an account</Link>
                  <br />
                  <p>Have an account? </p>
                  <Link id="login" to="/login">Login</Link>
                </div>
                )
                }
      </div>
    );
  }
}

export default SplashPage;
