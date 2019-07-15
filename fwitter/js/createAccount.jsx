import React from 'react';

class CreateAccount extends React.Component {
    constructor(props) {
        super(props);
    }

    componentDidMount() {
        //TODO make api call to check if user is logged in
    }

    render() {
        return(
        <p>this is the account creation page</p>
        );
    }
}

export default CreateAccount;
