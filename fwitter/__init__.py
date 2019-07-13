#!flask/bin/python
import os
from flask import Flask

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    database_temp = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'var', 'fwitter.sqlite3')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=database_temp
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    database_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'var')
    try:
        os.makedirs(database_folder)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from .api import api_bp
    app.register_blueprint(api_bp)

    from .base import base_bp
    app.register_blueprint(base_bp)

    return app
