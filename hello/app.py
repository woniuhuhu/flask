
from flask import Flask
app = Flask(__name__)
@app.route('/')
@app.route('/jh/<name>')
def index(name='jh'):
    return '<h1>Hello world,%s </h1>'%name 