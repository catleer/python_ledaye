"""
Created by catleer on 2018-09-08.
"""
__author__ = 'catleer'

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
from ..models import Permission


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
