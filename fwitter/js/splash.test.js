import React from 'react';
import { shallow } from 'enzyme';
import SplashPage from './splash';
import "isomorphic-fetch";

describe('Testing the spash page', () => {
    it('can render a page without logging in', () => {
       shallow(<SplashPage />);
     });
 });