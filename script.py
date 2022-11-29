# import main Flask class and request object
from flask import Flask, request

# create the Flask app
app = Flask(__name__)
@app.route('/')
def hello():
    # if key doesn't exist, returns None
    name = request.args.get('name')
    message = request.args.get('message')

    return print('''<h1>Hello, {}! {}</h1>'''.format(name,message))