import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

import flask
from . import api_bp
import fwitter
import requests
from fwitter.util.encrypt import hash_password
import pdb

@api_bp.route('/account', methods=['POST', 'DELETE'])
def create():
    """Add a new user to the database"""

    if(flask.request.method == 'POST'):
        request_data = flask.request.get_json()
                
        fullname = request_data['fullname']
        username = request_data['username']
        email = request_data['email']
        password = hash_password(request_data['password'])
        filename = request_data['filename']

        db = fwitter.db.get_db()
        cur = db.cursor()

        # Username is the primary key in users, so the code throws an exception if a duplicate is added
        try:
            cur.execute('''INSERT INTO users(fullname, username, email, password, filename) VALUES ('{}', '{}', '{}', '{}', '{}')'''
                        .format(fullname, username, email, password, filename))
        except:
            return {}, 403

        flask.session['username'] = username
        flask.session['email'] = email
        flask.session['fullname'] = fullname
        
        return {}, 201
    elif(flask.request.method == 'DELETE'):

        if 'username' not in flask.session:
            return {}, 403
        
        username = flask.session['username']
        
        db = fwitter.db.get_db()
        cur = db.cursor()

        cur.execute('DELETE FROM users WHERE username="{}"'.format(username))

        flask.session.pop('username', None)

        return {}, 204
    else:
        return {}, 403

@api_bp.route('/login', methods=['POST'])
def login():
    """Log a user in to their account"""

    if 'username' in flask.session:
        flask.abort(403)

    request_data = flask.request.get_json()

    username = request_data['username']
    password = hash_password(request_data['password'])

    db = fwitter.db.get_db()
    cur = db.cursor()

    # Get data based on username and compare
    
    try:
        print('username ' + username)
        cur.execute("SELECT * FROM users WHERE username='{}'".format(username))
    except:
        # Username not found
        flask.abort(401)
    
    data = cur.fetchall()
    if not data:
        # Username not found
        flask.abort(401)

    if data[0]['password'] != password:
        flask.abort(401)
    else:
        flask.session['username'] = username
        flask.session['email'] = data[0]['email']
        flask.session['fullname'] = data[0]['fullname']
        return {'username': flask.session['username']}, 200

@api_bp.route('/logout', methods=['GET'])
def logout():
    """Log a user out of a session"""

    if 'username' not in flask.session:
        flask.abort(403)

    flask.session.pop('username', None)
    flask.session.pop('email', None)
    flask.session.pop('fullname', None)

    return {}, 200

@api_bp.route('/check_login', methods=['GET'])
def check_login():
    """Check if a user is already logged in"""

    if 'username' not in flask.session:
        flask.abort(401)

    return {'username': flask.session['username']}, 200
