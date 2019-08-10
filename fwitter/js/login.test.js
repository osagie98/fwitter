/* eslint-disable react/jsx-filename-extension */
/* eslint-disable no-undef */
import React from 'react';
import { shallow, mount } from 'enzyme';
// eslint-disable-next-line no-unused-vars
import fetch from 'isomorphic-fetch';
import sinon from 'sinon';
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

describe('Login page when logged out', () => {
  let mockResponse;
  let wrapper;

  beforeEach(() => {
    mockResponse = {};

    window.fetch = jest.fn().mockImplementation(() => Promise.resolve({
      json: () => Promise.resolve(mockResponse),
      status: 401,
    }));
    wrapper = shallow(<Login />);
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

describe('Logging in on Login', () => {
  let mockResponse = { };
  let wrapper;


  beforeAll(() => {
    window.fetch = jest.fn().mockImplementation(() => Promise.resolve({
      json: () => Promise.resolve(mockResponse),
      status: 401,
    }));
    wrapper = shallow(<Login />);

    mockResponse = { username: 'osagie01' };
    window.fetch = jest.fn().mockImplementation(() => Promise.resolve({
      json: () => Promise.resolve(mockResponse),
      status: 200,
      ok: true,
    }));
  });

  it('starts with redirectToProfile being false', () => {
    expect(wrapper.state('redirectToProfile')).toEqual(false);
  });
  it('changes username on input', () => {
    wrapper.find('input#username').simulate('change', { target: { value: 'osaie01' } });
    expect(wrapper.state('username')).toEqual('osaie01');
  });
  it('changes password on input', () => {
    wrapper.find('input#password').simulate('change', { target: { value: 'thisIsATestPassword' } });
    expect(wrapper.state('password')).toEqual('thisIsATestPassword');
  });
  it('calls fetch on submit', () => {
    wrapper.find('form#login').simulate('submit');
    expect(window.fetch).toHaveBeenCalled();
    expect(wrapper.state('username')).toEqual('osagie01');
  });
  it('sets username to body username', () => {
    expect(wrapper.state('username')).toEqual('osagie01');
  });
  it('sets redirectToProfile to true', () => {
    expect(wrapper.state('redirectToProfile')).toEqual(true);
  });
  it('renders the redirect', () => {
    expect(wrapper.find('Redirect').props().to).toEqual(`/users/${wrapper.state('username')}`);
  });
});

describe('Logging in on Login with bad credentials', () => {
  const mockResponse = { };

  window.fetch = jest.fn().mockImplementation(() => Promise.resolve({
    json: () => Promise.resolve(mockResponse),
    status: 401,
  }));

  const wrapper2 = shallow(<Login />);

  window.fetch = jest.fn().mockImplementation(() => Promise.resolve({
    json: () => Promise.resolve(mockResponse),
    status: 403,
  }));

  it('should not change redirectToProfile to true on a bad login', () => {
    expect(wrapper2.state('redirectToProfile')).toEqual(false);
    wrapper2.find('input#username').simulate('change', { target: { value: 'osae01' } });
    wrapper2.find('input#password').simulate('change', { target: { value: 'thisIsATestPassword' } });
    wrapper2.find('input#submit').simulate('click');
    expect(window.fetch).toHaveBeenCalled();
    expect(wrapper2.state('redirectToProfile')).toEqual(false);
  });
});
