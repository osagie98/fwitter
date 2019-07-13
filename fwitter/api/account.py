import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

import flask
from . import api_bp
import fwitter
import requests
from fwitter.util.encrypt import hash_password

@api_bp.route('/account/create', methods=['POST'])
def create():
    """Add a new user to the database"""

    request_data = flask.request.form
            
    fullname = request_data['fullname']
    username = request_data['username']
    email = request_data['email']
    password = hash_password(request_data['password'])
    filename = request_data['filename']

    db = fwitter.db.get_db()
    cur = db.cursor()
            
    #TODO Fix returns

    # Because username is the primary key in users, the code throws an exception if a duplicate is added
    try:
        cur.execute("INSERT INTO users(fullname, username, email, password, filename) VALUES ('{}', '{}', '{}', '{}', '{}')".format(fullname, username, email, password, filename))
    except:
        return {}, 403

    return {}, 201
