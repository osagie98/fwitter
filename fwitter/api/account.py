from fwitter import app
from fwitter import database
from flask import Flask, render_template

@app.route('/login')
def login():

    return render_template('index.html')