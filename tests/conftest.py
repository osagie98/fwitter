# Flask boilerplate
import os
import tempfile

import pytest
from fwitter import create_app
from fwitter.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'test.sql'), 'rb') as f:
    _test_sql = f.read().decode('utf8')

#Create a temporary file for testing the database
@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_test_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()

class Cookie(object):
    def __init__(self, client):
        self._client = client

    def login(self, username, password):
        return self._client.post(
            '/api/v1/login',
            json={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/api/v1/logout')


@pytest.fixture
def cookie(client):
    return Cookie(client)
    