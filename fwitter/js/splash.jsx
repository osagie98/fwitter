import React from 'react';

class SplashPage extends React.Component {
    constructor(props) {
        super(props);
    }

    componentDidMount() {
        //TODO make api call to check if user is logged in
    }

    render() {
        return(
            <p>This place will ask you to login</p>
        );
    }
}

export default SplashPage;
