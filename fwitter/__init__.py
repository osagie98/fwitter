#!flask/bin/python
import os
from flask import Flask

app = Flask(__name__)

def create_app():
    app = ...
    # existing code omitted

    from . import database
    database.init_app(app)

    return app

app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join('var', 'flaskr.sqlite'),
    )

# File Upload to var/uploads/
UPLOAD_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'var', 'uploads'
)

import fwitter.views
