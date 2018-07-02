"""
Created by catleer on 2018-07-02.
"""

__author__ = 'catleer'
import sys
sys.path.append('.')
import json, codecs, os
print(os.getcwd())

def get_case():
    with codecs.open('data.json', 'r', encoding='utf-8') as f:
        f_dict = json.load(f)
        for collection, cases in f_dict.items():
            for case in cases['interface_info']:
                yield {collection: case}


def get_data():
    cases = get_case()
    # url_methods = []
    # methods = []
    # headerss = []
    # url_datas = []
    # datas = []
    # paramss = []
    # auths = []
    # cookiess = []
    # hookss = []
    # jsons = []
    # except_datas = []
    datas = []
    for case_d in cases:
        for collection, case in case_d.items():
            url_method = case['interface_method']
            method = case['method']
            headers = case["headers"]
            url_data = case['url_data'] # if case['url_data'] is None else tuple(case['url_data'])
            data = case['data']
            params = case['params']
            auth = case['auth']
            cookies = case['cookies']
            hooks = case['hooks']
            json = case['json']
            except_data = case['except']
            t = (url_method, method, headers, url_data, data, params, auth, cookies, hooks, json, except_data)
            datas.append(t)

    return datas

print(type(get_case()))
print(get_data())


