import React from 'react';
import ReactDOM from 'react-dom';
import { HashRouter, Route, Link } from 'react-router-dom';
import SplashPage from './splash';
import Login from './login';
import CreateAccount from './createAccount';
import Profile from './profile';

let App = () => {
    return(
        <HashRouter>
            {/* exact set to true to make sure only SplashPage renders at "/"*/}
            <Route exact={true} path="/" component={SplashPage}/>
            <Route path="/login" component={Login}/>
            <Route path="/create" component={CreateAccount}/>
            <Route path="/:user" component={Profile}/>
        </HashRouter>
    );
}

export default App;