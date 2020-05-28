'''
Loads config from environment variables
'''
import os

ENV_DEV = 'development' == os.getenv('FLASK_ENV', 'production')
DOMAINS = ['unc.edu', 'duke.edu']
COLLEGES = {
    'unc.edu': 'UNC-Chapel Hill',
    'duke.edu': 'Duke University'
}