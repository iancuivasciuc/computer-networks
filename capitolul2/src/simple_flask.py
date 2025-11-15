from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

'''
This method expects a json content.
Use header: 'Content-Type: application/json'
'''
@app.route('/post', methods=['POST'])
def post_method():
    print("Got from user: ", request.get_json())
    print(request.get_json()['value']*2)
    return jsonify({'got_it': 'yes'})

@app.route('/double')
def double_method_get():
    return jsonify({'double' : int(request.args['value']) * 2})

@app.route('/double', methods=['POST'])
def double_method_post():
    return jsonify({'double' : request.get_json()['value'] * 2})

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
