from fwitter.fwitterapp import app
from flask import Flask, redirect, url_for

@app.route('/')
def index():

    return 'test'