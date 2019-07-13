import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

import flask
from . import base_bp
import fwitter
import requests
from fwitter.util.encrypt import hash_password

@base_bp.route('/', methods=['GET'])
def index():
    """Landing page"""

    return flask.render_template("index.html")
