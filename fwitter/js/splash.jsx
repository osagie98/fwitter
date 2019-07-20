import React from 'react';
import Login from './login';
import { Link, Redirect } from 'react-router-dom';

class SplashPage extends React.Component {
    constructor(props) {
        super(props);

        this.onSubmit = this.onSubmit.bind(this)
    }
    
    onSubmit(event) {

    }

    componentDidMount() {
        //TODO make api call to check if user is logged in
        fetch('/api/v1/checkLogin', { credentials: 'omit' })
        .then((response) => {
          //if (!response.ok)
          return response.json();
        })
    }

    render() {
        return(
            <Link to="/login">Please login</Link>
        );
    }
}

export default SplashPage;
