import React from 'react';
// import ReactDOM from 'react-dom';
import { HashRouter, Route } from 'react-router-dom';
import SplashPage from './splash';
import Login from './login';
import Logout from './logout';
import CreateAccount from './createAccount';
import Profile from './profile';

const App = () => (
  <div id="maina-application">
    { /* exact set to true to make sure only SplashPage renders at "/" */}
    <Route exact path="/" component={SplashPage} />
    <Route path="/login" component={Login} />
    <Route path="/create" component={CreateAccount} />
    <Route path="/users/:user" component={Profile} />
    <Route path="/logout" component={Logout} />
  </div>
);

export default App;
