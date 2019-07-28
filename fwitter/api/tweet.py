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

@api_bp.route('/tweet', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def tweet():
    """Get a tweet from the database, or post a new one"""
    if 'username' not in flask.session:
        return {}, 403

    request_data = flask.request.form

    if flask.request.method == 'GET':
        return {}, 404
    elif flask.request.method == 'POST':
        # Cannot specify both body and id
        if 'body' in request_data and 'id' in request_data:
            return {}, 403
       
        if len(request_data) > 1:
            return {}, 403

        db = fwitter.db.get_db()
        cur = db.cursor()

        # Normal new tweet
        if 'body' in request_data:
            cur.execute('SELECT count(*) FROM tweets')
            tweetid = int(cur.fetchone()[0]) + 1
    
            cur.execute('''INSERT INTO tweets(body, tweetid, owner, originalOwner) VALUES
                        ('{}', '{}', '{}', '{}')'''.format(request_data['body'], tweetid,
                                                        flask.session['username'],
                                                        flask.session['username']))
            
            return {}, 201
        elif 'id' in request_data:
            return {}, 404
        else:
            return {}, 403
    elif flask.request.method == 'PATCH':
        return {}, 404
    elif flask.request.method == 'DELETE':
        return {}, 404
    else:
        return {}, 403