import React from 'react';
// import fetch from 'isomorphic-fetch';
// import { Link, Redirect } from 'react-router-dom';

class SplashPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = { redirectToProfile: true };
  }

  componentDidMount() {
    // TODO make api call to check if user is logged in
    // eslint-disable-next-line no-undef
    fetch('/api/v1/checkLogin', { credentials: 'omit' })
      .then((response) => {
        if (!response.ok) {
          if (response.status === 401) { /* Unauthorized error,
            ask user to create an account or log in */
            this.setState({ redirectToProfile: false });
          } else {
            throw Error(response.status);
          }
        }
        console.log('this should show up 6 times')
        return response;
      })
      .catch(error => console.log(error));
  }

  render() {
    const { redirectToProfile } = this.state;
    return (
      <div className="login-or-redirect">
        { redirectToProfile
                && <p className="test">test</p>
                }
        { !redirectToProfile
                && <div className="create-account" />
                }
      </div>
    );
  }
}

export default SplashPage;
