'''
Author: your name
Date: 2021-09-18 15:27:32
LastEditTime: 2021-09-18 15:29:24
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \flask\hello\app.py
'''
from flask import Flask
app = Flask(__name__)
@app.rote('/')
def index():
    return '<h1>Hello world</h1>'