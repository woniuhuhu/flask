'''
Author: your name
Date: 2021-09-18 15:27:32
LastEditTime: 2021-09-18 21:20:28
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \flask\hello\app.py
'''

from flask import Flask
app = Flask(__name__)
@app.route('/')
@app.route('/jh/<name>')
@app.route('/<name>')
def index(name='jcx'):
    return '<h1>Hello world,%s </h1>'%name 

@app.cli.command()
def hello():
    print('hello,jianghui')