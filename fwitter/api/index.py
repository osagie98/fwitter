from fwitter.fwitterapp import app
from flask import Flask, redirect, url_for

@app.route('/', methods=('GET'))
def index():

    return 'test'