"""
Created by catleer on 2018-06-26.
"""
from app import create_app

__author__ = 'catleer'

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
