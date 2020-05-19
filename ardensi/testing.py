'''
Testing script for ardensi api
'''
from flask import Flask, request, jsonify, abort

from ardensi.application import app


@app.route('/', methods=['GET'])
def hello():
    return 'Hello world!', 200

@app.route('/testing', methods=['POST'])
def test():
    req = request.json
    if req is None or req['username'] is None or req['message'] is None:
        return 'Could not handle that request.', 403
    user = req['username']
    message = req['message']
    thing, thing1 = req['test_dict']['first'], req['test_dict']['second']
    print(thing)
    print(thing1)

    ret = {
        'body': f'{user} said - {message} - at this time from neel runton.',
        'test_dic': {'first': 'can I do this?', 'second': 'from ur mom', 'third': 'you lost'}
    }
    return jsonify(ret), 200