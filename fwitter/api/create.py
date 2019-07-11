import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from . import api_bp

@api_bp.route('/create', methods=['GET'])
def create():
    print('test')
    return 'Hello Blueprint!'
    