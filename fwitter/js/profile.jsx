import React from 'react';

class Profile extends React.Component {
    constructor(props) {
        super(props);
    }

    componentDidMount() {
        //TODO make api call to check if user is logged in
        const { match: { params } } = this.props
        console.log(params.user)
    }

    render() {
        return(
        <p>this is the account creation page</p>
        );
    }
}

export default Profile;
