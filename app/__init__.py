# [SublimeLinter pep8-ignore:E402]
from flask import Flask

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
