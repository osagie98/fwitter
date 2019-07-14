import os
import fwitter
from fwitter.db import get_db
import pytest
from flask import session

class TestSession():
    """Testing logging in and out"""

    def test_login(self, app, client, cookie):
        """Testing that a user has access to the correct locations when logging"""

        test_username = 'osagie_01'
        test_password = 'thisIsATestPassword'

        # Assert a logged in user cannot log in again
        response = cookie.login(test_username, test_password)
       
        with client:
           client.get('/')
           assert session['username'] == 'osagie_01'
           assert session['email'] == 'osagie@umich.edu'
           assert session['fullname'] == 'Augustine Osagie'

        # TODO add error if logged in user logs in again
        