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

    # Username is the primary key in users, so the code throws an exception if a duplicate is added
    try:
        cur.execute("INSERT INTO users(fullname, username, email, password, filename) VALUES ('{}', '{}', '{}', '{}', '{}')".format(fullname, username, email, password, filename))
    except:
        return {}, 403

    flask.session['username'] = username
    flask.session['email'] = email
    flask.session['fullname'] = fullname
    
    return {}, 201

@api_bp.route('/login', methods=['POST'])
def login():
    """Log a user in to their account"""
    
    request_data = flask.request.form

    username = request_data['username']
    password = hash_password(request_data['password'])

    db = fwitter.db.get_db()
    cur = db.cursor()

    # Get data based on username and compare

    try:
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
        return {}, 200

@api_bp.route('/logout', methods=['GET'])
def logout():
    """Log a user out of a session"""

    if 'username' not in flask.session:
        flask.abort(403)

    flask.session.pop('username', None)
    flask.session.pop('email', None)
    flask.session.pop('fullname', None)

    return {}, 200

@api_bp.route('/checkLogin', methods=['GET'])
def checkLogin():
    """Check if a user is already logged in"""

    if 'username' not in flask.session:
        flask.abort(401)

    return {}, 200
