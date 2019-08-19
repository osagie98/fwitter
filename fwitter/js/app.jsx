import React from 'react';
import PropTypes from 'prop-types';
import { Route } from 'react-router-dom';
import SplashPage from './splash';
import Login from './login';
import Logout from './logout';
import CreateAccount from './createAccount';
import Profile from './profile';
import '../static/css/app.css';

class App extends React.PureComponent {
  render() {
    const { loggedIn } = this.props;
    return (
      <div id="main-application">
        { /* exact set to true to make sure only SplashPage renders at "/" */}
        <Route exact path="/" loggedIn={loggedIn} render={props => <SplashPage {...props} loggedIn={loggedIn} />} />
        <Route path="/login" loggedIn={loggedIn} render={props => <Login {...props} loggedIn={loggedIn} />} />
        <Route path="/create" loggedIn={loggedIn} render={props => <CreateAccount {...props} loggedIn={loggedIn} />} />
        <Route path="/users/:user" loggedIn={loggedIn} render={props => <Profile {...props} loggedIn={loggedIn} />} />
        <Route path="/logout" loggedIn={loggedIn} component={Logout} />
      </div>
    );
  }
}

export default App;

App.propTypes = {
  loggedIn: PropTypes.bool.isRequired,
};
