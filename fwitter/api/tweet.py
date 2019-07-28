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

    if flask.request.method == 'GET':
        return {}, 404
    elif flask.request.method == 'POST':
        
        return {}, 404
    elif flask.request.method == 'PATCH':
        return {}, 404
    elif flask.request.method == 'DELETE':
        return {}, 404
    else:
        return {}, 403