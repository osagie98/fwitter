import os
import fwitter
from fwitter.db import get_db
import pytest

class TestCreate():
    """Testing creating a new user"""

    def test_add_user(self, app, client):
        """Testing adding a new user with no data"""

        client.post('/api/v1/create', data={'username': 'test_user', 'fullname': 'Foo Bar', 'email': 'foozy@umich.edu', 'password': 'dontStoreInPlaintext', 'filename': 'testfile.jpg'})

        cursor = get_db().cursor()
        test = 'test'
        
        with pytest.raises(RuntimeError) as e:
            row = cursor.execute(f'SELECT * FROM USERS WHERE USERNAME = {test}')
            print(e)

        print(row)
        assert False
