import React from 'react';

class Login extends React.Component {
    constructor(props) {
        super(props);
    }

    componentDidMount() {
        //TODO make api call to check if user is logged in
    }

    render() {
        return(
        <p>This is the login page</p>
        );
    }
}

export default Login;
