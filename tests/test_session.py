"""Testing logging in and out."""
import os
import fwitter
from fwitter.db import get_db
import pytest
from flask import session
import pdb

class TestSession():
   """Testing logging in and out."""
   
   def test_login_and_out(self, app, client, cookie):
      """Testing that a user has access to the correct locations when logging."""
      test_username = 'osagie_01'
      test_password = 'thisIsATestPassword'

      # Assert a login response has a username
      response = cookie.login(test_username, test_password)

      assert response.get_json()['username'] == 'osagie_01'
       
      with client:
         client.get('/')
         assert session['username'] == 'osagie_01'
         assert session['email'] == 'osagie@umich.edu'
         assert session['fullname'] == 'Augustine Osagie'

      # Assert logging in again is forbidden
      response = cookie.login(test_username, test_password)
      assert response.status_code == 403
        
      response = cookie.logout()

      assert response.status_code == 200

      # Test that a logged out user cannot logout aagin

      response = cookie.logout()

      assert response.status_code == 403

      with client:
         client.get('/')
         assert 'username' not in session
         assert 'email' not in session
         assert 'fullname' not in session

      # Checking correct username but wrong password, and vice versa

      response = cookie.login(test_username, 'wrongPassword')

      assert response.status_code == 401

      response = cookie.login('wrongUsername', test_password)

      assert response.status_code == 401


   def test_check_login(self, app, client, cookie):
      """Testing api call to see if user is already logged in."""
      test_username = 'osagie_01'
      test_password = 'thisIsATestPassword'

      with client:
         response = client.get('/api/v1/check_login')

         assert response.status_code == 401

         cookie.login(test_username, test_password)

         response = client.get('/api/v1/check_login')

         assert response.status_code == 200
    
         assert response.get_json()['username'] == 'osagie_01'

      cookie.logout()

