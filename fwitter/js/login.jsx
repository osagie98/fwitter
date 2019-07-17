import React from 'react';

class Login extends React.Component {
    constructor(props) {
        super(props);
        this.state = { username: '', password: '' };
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
        fetch('/api/v1/login', { method: 'POST', credentials: 'same-origin', headers: {username: this.state.username, password: this.state.password} })
        .then((response) => {
          if (!response.ok) return <p>You're logged in on login!</p>;
          return response.json();
        })
    }

    componentDidMount() {
        //TODO make api call to check if user is logged in
    }

    render() {
        return(
        <form onSubmit={this.onSubmit}>
            <p>This is the login page</p><br />
            Username: <input type="text" onChange={this.onChangeUsername} /><br />
            Password: <input type="text" onChange={this.onChangePassword} /><br />
            <input type="submit"/>
        </form>
        );
    }
}

export default Login;
