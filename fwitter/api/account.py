from fwitter import app
from fwitter import database
from flask import Flask

@app.route('/login')
def login():

    return 'Hello again!'