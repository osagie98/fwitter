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
        fetch('http://localhost:5000/api/v1/checkLogin', { credentials: 'omit' })
        .then((response) => {
          if (!response.ok) throw Error(response.statusText);
          return response.json();
        })
        .catch(error => console.log(error));
    }

    render() {
        return(
            <div className="create-account" />
        );
    }
}

export default SplashPage;
