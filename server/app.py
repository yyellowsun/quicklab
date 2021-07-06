#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
import pymysql

# venv\Scripts\activate
# .\app.py
#yarn serve
#npm run lint 查看有没有错误
# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/open', methods=['GET'])
def open_door():
    return jsonify(u'芝麻开门！')


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run()