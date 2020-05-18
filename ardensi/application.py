from flask import Flask, request, jsonify, abort


app = Flask(__name__)

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

    ret = {
        'body': f'{user} said - {message} - at this time.'
    }
    return jsonify(ret), 200


if __name__ == '__main__':
    app.run(debug=True)