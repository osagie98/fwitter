import os
import fwitter
from fwitter.db import get_db
import pytest
from flask import session

class TestSession():
   """Testing logging in and out"""

   def test_login_and_out(self, app, client, cookie):
      """Testing that a user has access to the correct locations when logging"""

      test_username = 'osagie_01'
      test_password = 'thisIsATestPassword'

      # Assert a logged in user cannot log in again
      cookie.login(test_username, test_password)
       
      with client:
         client.get('/')
         assert session['username'] == 'osagie_01'
         assert session['email'] == 'osagie@umich.edu'
         assert session['fullname'] == 'Augustine Osagie'

      # TODO add error if logged in user logs in again
        
      cookie.logout()

      with client:
         client.get('/')
         assert 'username' not in session
         assert 'email' not in session
         assert 'fullname' not in session

   def test_check_login(self, app, client, cookie):
      """Testing api call to see if user is already logged in"""

      test_username = 'osagie_01'
      test_password = 'thisIsATestPassword'

      with client:
         response = client.get('/api/v1/checkLogin')

         assert response.status_code == 404

         cookie.login(test_username, test_password)

         response = client.get('/api/v1/checkLogin')

         assert response.status_code == 200

