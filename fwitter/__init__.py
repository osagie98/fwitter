#!flask/bin/python
from flask import Flask

app = Flask(__name__)

import fwitter.views
