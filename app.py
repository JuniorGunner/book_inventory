# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route('/index')
def hello():
    return '<h1>Hello Flask World!</h1>'

app.run()
