'''
Loads config from environment variables
'''
import os

ENV_DEV = 'development' in os.environ['FLASK_ENV']