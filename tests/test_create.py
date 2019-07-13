import os
import fwitter
from fwitter.db import get_db
import pytest

class TestCreate():
    """Testing creating a new user"""

    def test_add_user(self, app, client):
        """Testing adding a new user with no data"""

        client.post('/api/v1/create', data={'username': 'test_user', 'fullname': 'Foo Bar', 'email': 'foozy@umich.edu', 'password': 'dontStoreInPlaintext', 'filename': 'testfile.jpg'})
        with app.app_context():
            cursor = get_db()
            row = cursor.execute("SELECT * FROM users WHERE username = 'test_user'")
            
            data = row.fetchall()

            # Make sure the data is not empty
            assert data

            # Make sure all but password was inserte as expected
            assert data['username'] == 'test_user'
            assert data['fullname'] == 'Foo Bar'
            assert data['email'] == 'foozy@umich.edu'
            assert not data['password'] == 'dontStoreInPlaintext'
            assert data['filename'] == 'testfile.jpg'
            assert data['totaltweets'] == 0
            #TODO Find a way to test time created



