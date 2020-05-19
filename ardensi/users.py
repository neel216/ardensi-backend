'''
API functions for user account related actions
'''
from flask import request, jsonify, abort

from ardensi.application import app


@app.route('/user.signup', methods=['POST'])
def signup():
    req = request.json

    last_name = req['last_name']
    first_name = req['first_name']
    email = req['email']
    password = req['password']
    
    # check if email is taken - if it is, send back a 200 response but with a bad message
    # check if password is taken - if it is, send back a 200 response but with a bad message

    # check if email domain is a verified college email domain - if it isn't, send back a 200 response but with a bad message
    
    # determine what college the user goes to based on email and store it in variable
    
    # generate user_id
    # add user to db

    # return positive response

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