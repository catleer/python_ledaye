"""
Created by catleer on 2018-07-02.
"""
__author__ = 'catleer'
import sys
sys.path.append('.')

import pytest

from httpmethods import Http
import conftest

@pytest.mark.parametrize("url_method, method, headers, url_data, data, params, auth, cookies, hooks, json, except_data",
                         conftest.get_data())
def test_case(url_method, method, headers, url_data, data, params, auth, cookies, hooks, json, except_data):
    h = Http(method=method, url_method=url_method, headers=headers,
             url_data=url_data, data=data, params=params, auth=auth,
             cookies=cookies, hooks=hooks, json=json)
    r = h.method_new()
    assert r.status_code == except_data[0]


