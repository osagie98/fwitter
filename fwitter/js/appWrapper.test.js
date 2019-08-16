/* eslint-disable react/jsx-filename-extension */
/* eslint-disable no-undef */
import React from 'react';
import { shallow } from 'enzyme';
// eslint-disable-next-line no-unused-vars
import AppWrapper from './appWrapper';


describe('App Wrapper page when logged in', () => {
  let mockResponse;
  let wrapper;

  beforeEach(() => {
    mockResponse = { username: 'osagie_01' };

    window.fetch = jest.fn().mockImplementation(() => Promise.resolve({
      json: () => Promise.resolve(mockResponse),
      status: 200,
      ok: true,
    }));
    wrapper = shallow(<AppWrapper />);
  });

  it('should fetch from the api upon mounting', () => {
    expect(window.fetch).toHaveBeenCalled();
  });

  it('should set redirectToProfile to true when logged in', () => {
    expect(wrapper.state('loggedIn')).toEqual(true);
  });

  it('should set username to the returned username', () => {
    expect(wrapper.state('username')).toEqual('osagie_01');
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
    wrapper = shallow(<AppWrapper />);
  });

  it('should fetch from the api upon mounting', () => {
    expect(window.fetch).toHaveBeenCalled();
  });

  it('should set redirectToProfile to false when not logged in', () => {
    expect(wrapper.state('loggedIn')).toEqual(false);
  });

  it('should set username to the returned username', () => {
    expect(wrapper.state('username')).toEqual('');
  });
});
