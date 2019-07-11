#Flask boilerplate
from fwitter import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/api/v1/create')
    assert response.data == b'Hello Blueprint!'