import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from fwitter.db import get_db

# Provide base routes for those not logged in
base_bp = Blueprint('base', __name__, url_prefix='')

from . import create
