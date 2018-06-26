"""
Created by catleer on 2018-06-26.
"""
__author__ = 'catleer'


def is_isbn_or_key(word):
    """
    :param word: 传入的关键字
    :return: 返回关键字类型
    """
    # isbn13 isbn10
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_q = word.replace('-', '')
    if '-' in word and len(short_q) == 10 and short_q.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
