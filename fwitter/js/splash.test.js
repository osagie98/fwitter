/* eslint-disable react/jsx-filename-extension */
/* eslint-disable no-undef */
import React from 'react';
import { shallow } from 'enzyme';
import SplashPage from './splash';

describe('<SplashPage />', () => {
  it('can render a page without logging in', () => {
    shallow(<SplashPage />);
  });
});

describe('Splash page when logged in', () => {
  let mockResponse;

  beforeEach(() => {
    mockResponse = {};

    window.fetch = jest.fn().mockImplementation(() => Promise.resolve({
      json: () => Promise.resolve(mockResponse),
    }));
  });

  it('should fetch from the api upon mounting', () => {
    // const wrapper = shallow(<SplashPage />);

    expect(window.fetch).toHaveBeenCalled();
  });

  it('should set redirectToProfile to true when logged in', () => {
    const wrapper = shallow(<SplashPage />);

    expect(wrapper.state('redirectToProfile')).toEqual(true);
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

  it('should set redirectToProfile to true when not logged in', () => {
    expect(wrapper.state('redirectToProfile')).toEqual(false);
  });

  it('renders the create-account div', () => {
    const wrapper2 = shallow(<SplashPage />);
    expect(wrapper2.find('.create-account')).to.have.length(1);
  });
});
