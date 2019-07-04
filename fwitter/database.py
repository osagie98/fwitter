import sqlite3
from flask import g
import fwitter

DATABASE = '/var/sqlite'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(fwitter.app.config['DATABASE'])
    return db

@fwitter.app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()