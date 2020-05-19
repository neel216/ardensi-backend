'''
Initialize Flask app and set debug mode
Import ardensi api modules for proper routing
'''
from flask import Flask

from ardensi import config


app = Flask(__name__)
app.debug = config.ENV_DEV

# Import all files for proper routing here
import ardensi.testing