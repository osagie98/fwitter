import os
import fwitter
from fwitter.util.encrypt import hash_password, compare_passwords
import pytest

class TestEncrypt():
    """Testing creating a new user"""

    def test_hash(self):
        """Testing hashing a password"""
        test_password = 'testing'
        test_hash = hash_password(test_password)

        assert test_password != test_hash
        


    def test_compare_password(self):
        """Testing comparing hashed passwords for logging in"""

        test_password = 'testing'
        test_password_2 = 'ijustlovetestcases'

        test_hash = hash_password(test_password)

        assert not compare_passwords(test_password_2, test_hash)

        test_password_3 = 'testing'
        assert compare_passwords(test_password_3, test_hash)

