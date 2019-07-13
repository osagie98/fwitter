import os
import fwitter
from fwitter.db import get_db
import pytest
from flask import session

class TestSession():
    """Testing logging in and out"""

    def test_login(self, app, client):
        """Testing that a user has access to the correct locations when logging"""

        test_username = 'osagie_01'
        test_password = 'thisIsATestPassword'

        # Assert some areas can be accessed without logging in
        