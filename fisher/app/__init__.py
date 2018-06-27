"""
Created by catleer on 2018-06-27.
"""
from flask import Flask

__author__ = 'catleer'


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_web_blueprint(app)
    return app


def register_web_blueprint(app):
    from app.web import web
    app.register_blueprint(web)


