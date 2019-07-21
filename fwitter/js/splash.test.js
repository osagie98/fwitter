import React from 'react';
import { shallow } from 'enzyme';
import SplashPage from './splash';
import "isomorphic-fetch";
import nock from 'nock';

describe('<SplashPage />', () => {
    it('can render a page without logging in', () => {
       shallow(<SplashPage />);
     });
 });

 describe('A new Splash page test', () => {

  nock('http://localhost:5000/api/v1/checkLogin')
      .get('')
      .reply(404);
  it('can look for certain text', () => {
     const wrapper = shallow(<SplashPage />);

     expect(wrapper.find('div.create-account')).to.have.lengthOf(1);
   });
});