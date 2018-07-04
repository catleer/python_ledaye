"""
Created by catleer on 2018-05-21.
"""
__author__ = 'catleer'

import unittest

import pytest
import sys
sys.path.append('.')
from common import get_casedata
from common import httpmethods
# from common import send_email
import ddt
import paramunittest
# 生成测试用例

case_data = [case for case in get_casedata.get_case_data()]

@paramunittest.parametrized
class TestCases(unittest.TestCase):

    def test_case(self, url_method, method, headers, url_data, data, params, auth, cookies, hooks, json, result):
        h = httpmethods.Http(method=method, url_method=url_method, headers=headers,
                 url_data=url_data, data=data, params=params, auth=auth,
                 cookies=cookies, hooks=hooks, json=json)
        r = h.method_new()


if __name__ == '__main__':
    print(case_data)