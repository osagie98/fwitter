import React from 'react';
import { shallow } from 'enzyme';
import SplashPage from './splash';
import "isomorphic-fetch";

describe('<SplashPage />', () => {
    it('can render a page without logging in', () => {
       shallow(<SplashPage />);
     });
 });

describe('A new Splash page test', () => {
 
  let mockResponse

  beforeEach(() => {
    mockResponse = {}

    window.fetch = jest.fn().mockImplementation(() => Promise.resolve({
      json: () => Promise.resolve(mockResponse)
    }))
  })

  it('should fetch from the api upon mounting', () => {

     const wrapper = shallow(<SplashPage />);

     //expect(wrapper.find('div.create-account')).to.have.lengthOf(1);
     expect(window.fetch).toHaveBeenCalled()
   });

   it('should set redirectToProfile to true when logged in', () => {

    const wrapper = shallow(<SplashPage />);

    //expect(wrapper.find('div.create-account')).to.have.lengthOf(1);
    expect(wrapper.state('redirectToProfile')).toEqual(true)
  });
});