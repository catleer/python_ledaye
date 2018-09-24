"""
Created by catleer on 2018-05-21.
"""
from flask import Blueprint

__author__ = 'catleer'

web = Blueprint('web', __name__)

from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
# from app.web import user
