#!flask/bin/python
import os
from flask import Flask

app = Flask(__name__)

app.config.from_object('fwitter.config')

import fwitter.api.index
import fwitter.api.account
