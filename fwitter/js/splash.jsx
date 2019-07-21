import React from 'react';
import Login from './login';
import { Link, Redirect } from 'react-router-dom';

class SplashPage extends React.Component {
    constructor(props) {
        super(props);
        this.state = { redirectToProfile: true }

        this.onSubmit = this.onSubmit.bind(this)
    }
    
    onSubmit(event) {

    }

    componentDidMount() {
        //TODO make api call to check if user is logged in
        fetch('/api/v1/checkLogin', { credentials: 'omit' })
        .then((response) => {
          if (!response.ok) 
          {
            if (response.status === 401) 
            { // Unauthorized error, ask user to create an account or log in
                this.setState({ redirectToProfile: false })
            } else {
                throw Error(response.status);
            }
          }
          return response;
        })
        .catch(error => console.log(error));
    }

    render() {
        return(
            <div className="login-or-redirect">
                { this.state.redirectToProfile &&
                    <p>test</p>
                }
                { !this.state.redirectToProfile && 
                <div className="create-account" />
                }
            </div>
        );
    }
}

export default SplashPage;
