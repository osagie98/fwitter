"""Testing api calls related to following users."""
import os
import fwitter
from fwitter.db import get_db
import pytest
from flask import session
import pdb

class TestFollow():
    """Testing api calls related to following users."""

    def test_follow_users(self, app, client, cookie):
        """Test that a logged in user may follow an account"""
        test_username = 'osagie_01'
        test_password = 'thisIsATestPassword'

        # Test that a non logged in user cannot follow an account
        response = client.post('/api/v1/follow', json={ 'user': 'osagie_01'})

        assert response.status_code == 403

        cookie.login(test_username, test_password)

        with app.app_context():
            
            # Test that a logged in user can follow another user
            response = client.post('/api/v1/follow', json={ 'user': 'osagie_01'})

            assert response.status_code == 204
