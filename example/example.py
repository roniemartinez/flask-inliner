#!/usr/bin/python
__author__ = 'Ronie Martinez'
from flask import Flask
from flask_inliner import Inliner
app = Flask(__name__)
Inliner(app)


@app.route('/')
def hello_world():
    return '<html><head><style>h1 { color:#ffcc00; }</style></head><body><h1>Hello World!</h1></body></html>'

if __name__ == '__main__':
    app.run(debug=True)
