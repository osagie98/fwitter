/* eslint-disable react/jsx-filename-extension */
/* eslint-disable no-undef */
import React from 'react';
import { shallow } from 'enzyme';
// eslint-disable-next-line no-unused-vars
import fetch from 'isomorphic-fetch';
import SplashPage from './splash';


describe('<SplashPage />', () => {
  it('can render a page without logging in', () => {
    shallow(<SplashPage />);
  });
});

describe('Splash page when logged in', () => {
  let mockResponse;
  let wrapper;

  beforeEach(() => {
    mockResponse = { username: 'osagie_01' };

    window.fetch = jest.fn().mockImplementation(() => Promise.resolve({
      json: () => Promise.resolve(mockResponse),
      status: 200,
      ok: true,
    }));
    wrapper = shallow(<SplashPage />);
  });

  it('should fetch from the api upon mounting', () => {
    shallow(<SplashPage />);

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
    wrapper = shallow(<SplashPage />);
  });

  it('should fetch from the api upon mounting', () => {
    expect(window.fetch).toHaveBeenCalled();
  });

  it('should set redirectToProfile to false when not logged in', () => {
    expect(wrapper.state('redirectToProfile')).toEqual(false);
  });

  it('renders the create-account p', () => {
    expect(wrapper.find('.create-account-or-login')).toHaveLength(1);
  });
  it('renders the login Link', () => {
    expect(wrapper.find('Link#login').props().to).toEqual('/login');
  });
  it('renders the create Link', () => {
    expect(wrapper.find('Link#create').props().to).toEqual('/create');
  });
});
