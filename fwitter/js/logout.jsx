import React from 'react';
import { Redirect } from 'react-router-dom';
import fetch from 'isomorphic-fetch';

const Logout = () => {

    const { redirect } = this.state;
    return (
      <div>
        { !redirect
            && (
            <form onSubmit={this.onSubmit}>
              <p>This is the login page</p>
              <br />
                Username:
              {' '}
              <input type="text" onChange={this.onChangeUsername} />
              <br />
                Password:
              {' '}
              <input type="text" onChange={this.onChangePassword} />
              <br />
              <input type="submit" />
            </form>
            )
            }
        { redirect
                && <Redirect to="/" />
            }
      </div>
    );
}

export default Logout;
