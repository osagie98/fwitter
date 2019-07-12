import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

import flask

from . import api_bp
import fwitter

@api_bp.route('/create', methods=['GET', 'POST'])
def create():

    if flask.request.method == 'GET':
        cur = fwitter.db.get_db().cursor()
        cur.execute('select * from users')
        test = cur.fetchall()
        print(test[0]['username'])
        
        return 'Hello Blueprint!'
    else:

        return 'This is a POST'
    