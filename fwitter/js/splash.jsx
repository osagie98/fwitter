import React from 'react';
import fetch from 'isomorphic-fetch';
// import { Link, Redirect } from 'react-router-dom';

class SplashPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = { redirectToProfile: true };

    this.onSubmit = this.onSubmit.bind(this);
  }

  componentDidMount() {
    // TODO make api call to check if user is logged in
    fetch('/api/v1/checkLogin', { credentials: 'omit' })
      .then((response) => {
        if (!response.ok) {
          if (response.status === 401) { /* Unauthorized error,
            ask user to create an account or log in */
            console.log('setting state');
            this.setState({ redirectToProfile: false });
          } else {
            console.log('uh oh');
            throw Error(response.status);
          }
        }
        return response;
      })
      .catch(error => console.log(error));
  }

  render() {
    const { redirectToProfile } = this.state;
    return (
      <div className="login-or-redirect">
        { redirectToProfile
                && <p>test</p>
                }
        { !redirectToProfile
                && <div className="create-account" />
                }
      </div>
    );
  }
}

export default SplashPage;
