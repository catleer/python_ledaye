"""
Created by catleer on 2018-07-02.
"""
__author__ = 'catleer'


import json, codecs, os
print(os.getcwd())

from requests import Request

from httpmethods import Http


def get_case():
    with codecs.open('data.json', 'r', encoding='utf-8') as f:
        f_dict = json.load(f)
        for collection, cases in f_dict.items():
            for case in cases['interface_info']:
                yield {collection: case}


def run():
    cases = get_case()
    for case_d in cases:
        for collection, case in case_d.items():
            url_method = case['interface_method']
            method = case['method']
            headers = case["headers"]
            url_data = tuple(case['url_data'])
            data = case['data']
            params = case['params']
            auth = case['auth']
            cookies = case['cookies']
            hooks = case['hooks']
            json = case['json']
            except_data = case['except']

            h = Http(method=method, url_method=url_method, headers=headers,
                     url_data=url_data, data=data, params=params, auth=auth,
                     cookies=cookies, hooks=hooks, json=json)
            r = h.method_new()
            print(r)
run()


