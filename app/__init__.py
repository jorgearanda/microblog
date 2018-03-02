# [SublimeLinter pep8-ignore:E402]
from flask import Flask

app = Flask(__name__)

from app import routes
