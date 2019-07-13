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
            #row = cursor.execute('SELECT * FROM USERS')
            #print(row.fetchall())

        assert False
