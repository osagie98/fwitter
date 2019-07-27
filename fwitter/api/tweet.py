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

@api_bp.route('/tweet', methods=['GET', 'POST'])
def tweet():
    """Get a tweet from the database, or post a new one"""


@api_bp.route('/like_tweet')
def like_tweet():
    """Post a like to a requested tweet"""

    if flask.request.method == 'GET':
        print('test')
    elif flask.request.method == 'POST':
        print('test')
    else:
        return {}, 403