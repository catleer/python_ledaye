"""
Created by catleer on 2018-06-27.
"""
from flask import Flask

from app.models.book import db

__author__ = 'catleer'


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.settings')

    register_web_blueprint(app)
    db.init_app(app)
    db.create_all(app=app)
    return app


def register_web_blueprint(app):
    from app.web import web
    app.register_blueprint(web)


