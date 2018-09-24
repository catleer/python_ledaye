"""
Created by catleer on 2018-06-27.
"""
import json

from flask import jsonify, request, render_template, flash

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm
from app.view_models.book import BookViewModel
from app.view_models.book import BookCollection
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
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)

        # return json.dumps(books, default=lambda o: o.__dict__)
        # return jsonify(books.__dict__)
    else:
        flash("输入的搜索关键字不符合要求，请重新输入")
        # return jsonify(form.errors)
    return render_template('search_result.html', books=books)


@web.route('/test')
def test():
    r = {
        'name': 'lele',
        'age': 18
    }
    flash('hello, i am a message')
    return render_template('test.html', data=r)

