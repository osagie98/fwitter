/* eslint-disable react/jsx-filename-extension */
/* eslint-disable no-undef */
import React from 'react';
import { shallow, mount } from 'enzyme';
// eslint-disable-next-line no-unused-vars
import fetch from 'isomorphic-fetch';
import SplashPage from './splash';
import Login from './login';


describe('<Login />', () => {
  it('can render a page without logging in', () => {
    shallow(<Login />);
  });
});

describe('Login page when logged in', () => {
  let mockResponse;
  let wrapper;

  beforeEach(() => {
    mockResponse = { username: 'osagie_01' };

    window.fetch = jest.fn().mockImplementation(() => Promise.resolve({
      json: () => Promise.resolve(mockResponse),
      status: 200,
      ok: true,
    }));
    wrapper = shallow(<Login />);
  });

  it('should fetch from the api upon mounting', () => {
    shallow(<Login />);

    expect(window.fetch).toHaveBeenCalled();
  });

  it('should set redirectToProfile to true when logged in', () => {
    expect(wrapper.state('redirectToProfile')).toEqual(true);
  });

  it('should set username to the returned username', () => {
    expect(wrapper.state('username')).toEqual('osagie_01');
  });

  it('should render a Redirect object to /profile', () => {
    expect(wrapper.find('Redirect')).toHaveLength(1);
    // Redirect to the page of the logged in user
    expect(wrapper.find('Redirect').props().to).toEqual(`/users/${wrapper.state('username')}`);
  });
});

describe('Splash page when logged out', () => {
  let mockResponse;
  let wrapper;

  beforeEach(() => {
    mockResponse = {};

    window.fetch = jest.fn().mockImplementation(() => Promise.resolve({
      json: () => Promise.resolve(mockResponse),
      status: 401,
    }));
    wrapper = mount(<SplashPage />);
  });

  it('should fetch from the api upon mounting', () => {
    expect(window.fetch).toHaveBeenCalled();
  });

  it('should set redirectToProfile to false when not logged in', () => {
    expect(wrapper.state('redirectToProfile')).toEqual(false);
  });

  it('renders the login form', () => {
    expect(wrapper.find('form#login')).toHaveLength(1);
  });
  it('renders the username input', () => {
    expect(wrapper.find('input#username')).toHaveLength(1);
  });
  it('renders the password input', () => {
    expect(wrapper.find('input#password')).toHaveLength(1);
  });
  it('renders the submit input', () => {
    expect(wrapper.find('input#submit')).toHaveLength(1);
  });
});
