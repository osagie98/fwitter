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
        if flask.request.method != 'GET':
            flask.abort(403)

    request_data = flask.request.form
    db = fwitter.db.get_db()
    cur = db.cursor()
    context = {}

    if flask.request.method == 'GET':
        if len(flask.request.args) == 0:
            flask.abort(403)
        
        args = flask.request.args.to_dict()

        if 'tweetid' not in args:
            flask.abort(404)

        cur.execute('SELECT * FROM tweets WHERE tweetid="{}"'.format(args['tweetid']))
        tweet = cur.fetchone()
        
        # Tweet not found
        if tweet == None:
            flask.abort(404)
        
        context['originalOwner'] = tweet[0] 
        context['body'] = tweet[1] 
        context['tweetid'] = tweet[2] 
        context['created'] = tweet[3] 
        context['owner'] = tweet[4] 
        context['likes'] = tweet[5]

        return flask.jsonify(**context), 200 
    elif flask.request.method == 'POST':
        # Cannot specify both body and id
        if 'body' in request_data and 'id' in request_data:
            flask.abort(403)
       
        if len(request_data) > 1:
            flask.abort(403)

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
            # Retweet

            tweetid = request_data['id']

            cur.execute('SELECT * FROM tweets WHERE tweetid="{}"'.format(tweetid))
            tweet = cur.fetchone()
        
            # Tweet not found
            if tweet == None:
                flask.abort(404)
            
            context['originalOwner'] = tweet[0] 
            context['body'] = tweet[1] 
            context['created'] = tweet[3] 
            context['owner'] = tweet[4] 
            context['likes'] = tweet[5]

            # Determine new tweetid
            cur.execute('SELECT count(*) FROM tweets')
            context['tweetid'] = int(cur.fetchone()[0]) + 1

            cur.execute('''INSERT INTO tweets(body, tweetid, owner, originalOwner) VALUES
                        ('{}', '{}', '{}', '{}')'''.format(context['body'], context['tweetid'],
                                                        flask.session['username'],
                                                        context['originalOwner']))

            return {}, 201
        else:
            flask.abort(403)
    elif flask.request.method == 'PATCH':
        flask.abort(404)
    elif flask.request.method == 'DELETE':
        flask.abort(404)
    else:
        flask.abort(403)