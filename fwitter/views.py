from fwitter import app
from fwitter import database
from flask import Flask
import sqlite3

@app.route('/')
def index():
    cur = database.get_db().cursor()
    print(cur)
    return 'Hello World!'
    