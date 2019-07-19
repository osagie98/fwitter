import React from 'react';
import { Redirect } from 'react-router-dom';

class Login extends React.Component {
    constructor(props) {
        super(props);
        this.state = { username: '', password: '', redirect: false };
        this.onSubmit = this.onSubmit.bind(this);
        this.onChangeUsername = this.onChangeUsername.bind(this);
        this.onChangePassword = this.onChangePassword.bind(this);
    }

    onChangePassword(event) {

        this.setState({
            password: event.target.value
          });
    }

    onChangeUsername(event) {
        this.setState({
            username: event.target.value
          });
    }
    
    onSubmit(event) {
        fetch('/api/v1/login', { method: 'POST', credentials: 'same-origin', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({username: this.state.username, password: this.state.password}) })
        .then((response) => {
            if (!response.ok) throw Error(response.statusText);
            return response.json();
          })
          .then((data) => {
            this.setState({
              redirect: true,
            });
          })
          .catch(error => console.log(error));
    }

    componentDidMount() {
        //TODO make api call to check if user is logged in
        fetch('/api/v1/checkLogin', { credentials: 'omit' })
        .then((response) => {
            if (!response.ok) throw Error(response.statusText);
            console.log(response)
            return response.json();
          })
          .catch(error => console.log(error));
    }

    render() {
        return(
        <div>
            { !this.state.redirect &&
            <form onSubmit={this.onSubmit}>
                <p>This is the login page</p><br />
                Username: <input type="text" onChange={this.onChangeUsername} /><br />
                Password: <input type="text" onChange={this.onChangePassword} /><br />
                <input type="submit"/>
            </form>
            }
            { this.state.redirect &&
                <Redirect to="/"/>
            }
        </div>
        );
    }
}

export default Login;
