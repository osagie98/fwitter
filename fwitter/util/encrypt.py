import uuid
import hashlib

def hash_password(password):
    salt = 'sha512'

    # Must encode before hashing or an error is thrown
    return hashlib.sha512(password.encode() + salt.encode()).hexdigest() + ':' + salt

def compare_passwords(new_password, db_password):
    # New password is passed in as plaintext, db password is encrypted
    return hash_password(new_password) == db_password
