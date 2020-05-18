'''
Loads config from environment variables
'''
import os

ENV_DEV = 'development' in os.getenv('FLASK_ENV', 'production')