"""
Created by catleer on 2018-06-27.
"""
from flask import jsonify

from helper import is_isbn_or_key
from yushu_book import YuShuBook
from . import web

__author__ = 'catleer'


@web.route('/book/search/<q>/<page>')
def search(q, page):
    """
    q: 关键字 isbn
    page:
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)

