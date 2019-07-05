from fwitter import app
from fwitter import database
from flask import Flask, redirect, url_for
from fwitter.api.account import login

@app.route('/')
def index():

    return redirect(url_for('login'))
    