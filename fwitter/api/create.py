import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

import flask
from . import api_bp
import fwitter
import requests

@api_bp.route('/create', methods=['GET', 'POST'])
def create():

    if flask.request.method == 'GET':
        cur = fwitter.db.get_db().cursor()
        cur.execute('select * from users')
        test = cur.fetchall()
        print(test[0]['username'])
        
        return 'Hello Blueprint!'
    else:

        request_data = request.get_json()
        fullname = request_data['fullname']
        username = request_data['username']
        email = request_data['email']
        password = request_data['password']
        filename = request_data['filename']
        return 'This is a POST'
    