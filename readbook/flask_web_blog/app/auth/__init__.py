"""
Created by catleer on 2018-09-08.
"""
__author__ = 'catleer'

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views