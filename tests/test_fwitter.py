import os
import tempfile

import pytest
'''
from fwitter import fwitter

@pytest.fixture
def client():
    db_fd, fwitter.app.config['DATABASE'] = tempfile.mkstemp()
    fwitter.app.config['TESTING'] = True
    client = fwitter.app.test_client()

    with fwitter.app.app_context():
        fwitter.init_db()

    yield client
    os.close(db_fd)
    os.unlink(fwitter.app.config['DATABASE'])
'''