"""
Created by catleer on 2018-06-28.
"""
__author__ = 'catleer'

from flask import Flask, current_app

app = Flask(__name__)

# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']

with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']

"""
上下文管理器协议：__enter__ __exit__
上下文管理器必须返回一个上下文对象
"""