"""
Created by catleer on 2018-06-27.
"""
from flask import jsonify, request

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook

from app.forms.book import SearchForm
from . import web

__author__ = 'catleer'


@web.route('/book/search')
def search():
    """
    q: 关键字 isbn
    page:
    ?q=isbn&page=1
    :return:
    """
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q)
        return jsonify(result)
    else:
        return jsonify(form.errors)

