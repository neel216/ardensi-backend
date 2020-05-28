'''
API functions for user account related actions
'''
from flask import request, jsonify, abort
from uuid import uuid4
from datetime import datetime

from ardensi.application import app
from ardensi.config import DOMAINS, COLLEGES
import ardensi.database as db


@app.route('/user.signup', methods=['POST'])
def signup():
    req = request.json

    first = req['first']
    last = req['last']
    email = req['email']
    password = req['password']
    
    if db.compareUserCreds('email', email) or db.compareUserCreds('password', password):
        ret = {
            'message': 'email and password must be unique'
        }
        return jsonify(ret), 200
    
    domain = email.split('@')[1]
    if domain not in DOMAINS:
        ret = {
            'message': 'email must be from a registered campus domain'
        }
        return jsonify(ret), 200

    user = {
        'time_created': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'first_name': first,
        'last_name': last,
        'email': email,
        'password': password,
        'college': COLLEGES[domain]
    }

    db.addUser(user)

    ret = {
        'message': 'user created'
    }

    return jsonify(ret), 200

@app.route('/user.login', methods=['POST'])
def login():
    req = request.json

    email = req['email']
    password = req['password']

    # check if email is in db - if it doesn't, send back a 200 response but with a bad message
    # if email is in db, check if password in db corresponds to that email - if it doesn't, send back a 200 response but with a bad message

    # return positive response

@app.route('/user.get', methods=['POST'])
def get_user():
    req = request.json

    user_id = req['user_id']

    # search db for user with user_id and return all of their info (except password)

    # return positive response and all of user's info (except password)

'''
# Save for last
@app.route('/user.updateAccount', methods=['POST'])
def update_account():
    req = request.json

    action = req['action'] # last_name, first_name, email, or password
    user_id = req['user_id']

    # if action is email, check if email domain is a registered college email domain

    # change user's chosen action in db

    # return positive response
'''

@app.route('/user.deleteAccount', methods=['POST'])
def delete_account():
    req = request.json

    user_id = req['user_id']

    # delete user from db

    # return positive response