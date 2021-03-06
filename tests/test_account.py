import os
import fwitter
from fwitter.db import get_db
from fwitter.util.encrypt import hash_password
import pytest
import sqlite3

class TestAccount():
    """Testing creating a new user"""

    def test_add_user(self, app, client, cookie):
        """Testing adding a new user with no data"""

        client.post('/api/v1/account', json={'username': 'test_user', 'fullname': 'Foo Bar', 'email': 'foozy@umich.edu', 'password': 'dontStoreInPlaintext', 'filename': 'testfile.jpg'})
        with app.app_context():
            cursor = get_db()
            row = cursor.execute("SELECT * FROM users WHERE username = 'test_user'")
            
            data = row.fetchall()

            # Make sure the data is not empty
            assert data

            # Make sure all but password was inserted as expected
            assert data[0]['username'] == 'test_user'
            assert data[0]['fullname'] == 'Foo Bar'
            assert data[0]['email'] == 'foozy@umich.edu'
            assert not data[0]['password'] == 'dontStoreInPlaintext'
            assert data[0]['password'] == hash_password('dontStoreInPlaintext')
            assert data[0]['filename'] == 'testfile.jpg'
            assert data[0]['totaltweets'] == 0
            #TODO Find a way to test time created

            cookie.logout()


    def test_add_duplicate(self, app, client):
        """Testing to ensure two users with the same username cannot both exist"""

        client.post('/api/v1/account', json={'username': 'test_user', 'fullname': 'Foo Bar', 'email': 'foozy@umich.edu', 'password': 'dontStoreInPlaintext', 'filename': 'testfile.jpg'})
        client.post('/api/v1/account', json={'username': 'test_user', 'fullname': 'Pro Gram', 'email': 'grammy@umich.edu', 'password': 'pleaseStoreInPlaintext', 'filename': 'testfile2.jpg'})
       
        with app.app_context():
            cursor = get_db()
            row = cursor.execute("SELECT * FROM users WHERE username = 'test_user'")
            
            data = row.fetchall()

            # Make sure the data is not empty
            assert len(data) == 1

    # TODO write a test for deleting an account
    def test_delete_account(self, app, client, cookie):
        """Testing to ensure that accounts are effectively deleted"""

        test_username = 'osagie01'
        test_password = 'thisIsATestPassword'

        # Assert that a logged out user cannot delete an account

        with client:
            response = client.delete('/api/v1/account')
            assert response.status_code == 403

        cookie.login(test_username, test_password)

        with client:
            # Normal test
            response = client.delete('/api/v1/account')
            assert response.status_code == 204
            
            cur = get_db().cursor()
            # Test that an error ocurrs when searching for the deleted account
            with pytest.raises(sqlite3.OperationalError) as e:
                cur.execute("SELECT * FROM users WHERE username=osagie01")

            assert 'no such column' in str(e.value)

            with pytest.raises(sqlite3.OperationalError) as e:
                cur.execute("SELECT * FROM tweets WHERE owner=osagie01")

            assert 'no such column' in str(e.value)
        
        # Not logging out here, that may cause issues
