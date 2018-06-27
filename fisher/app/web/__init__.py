"""
Created by catleer on 2018-06-27.
"""
from flask import Blueprint

__author__ = 'catleer'

web = Blueprint('web', __name__)

from app.web import book

