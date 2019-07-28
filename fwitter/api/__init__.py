import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from fwitter.db import get_db


api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

from . import account
from . import tweet
