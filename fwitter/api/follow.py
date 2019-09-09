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

@api_bp.route('/follow', methods=['POST', 'DELETE'])
def follow():
    """Follow or unfollow other accounts"""
    if 'username' not in flask.session:
        flask.abort(403)

    db = fwitter.db.get_db()
    cur = db.cursor()
    request_data = flask.request.get_json()

    if(flask.request.method == 'POST'):
        cur.execute('SELECT * FROM follow WHERE user1="{}" AND user2="{}"'.format(flask.session['username'], request_data['user']))
        follow = cur.fetchone()

        if follow != None:
            # Abort if user tries to follow a user they're already following
            flask.abort(403)

        cur.execute('INSERT INTO follow(user1, user2) VALUES ("{}", "{}")'.format(flask.session['username'], request_data['user']))

        return {}, 204
    elif (flask.request.method == 'DELETE'):
        cur.execute('SELECT * FROM follow WHERE user1="{}" AND user2="{}"'.format(flask.session['username'], request_data['user']))
        follow = cur.fetchone()

        if follow == None:
            # Abort if user tries to unfollow a user they're not following
            flask.abort(403)
        
        cur.execute('DELETE FROM follow WHERE user1="{}" AND user2="{}"'.format(flask.session['username'], request_data['user']))

        return {}, 202