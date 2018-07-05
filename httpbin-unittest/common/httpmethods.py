"""
Created by catleer on 2018-07-02.
"""
__author__ = 'catleer'
import sys
sys.path.append('.')
from urllib.parse import urljoin

import requests
from requests import Request, Session

from . import config

# print(config.BASE_URL)
class Http:
    def __init__(self,
                 method=None, url=None, headers=None, files=None, data=None,
                 params=None, auth=None, cookies=None, hooks=None, json=None,
                 base_url=None, url_method=None, url_data=None):
        # Default empty dicts for dict params.
        data = [] if data is None else data
        files = [] if files is None else files
        headers = {} if headers is None else headers
        params = {} if params is None else params
        hooks = {} if hooks is None else hooks
        url_data = () if url_data is None else tuple(url_data)
        auth = None if auth is None else tuple(auth)

        self.hooks = requests.hooks.default_hooks()
        type(hooks)
        for (k, v) in list(hooks.items()):
            Request.register_hook(event=k, hook=v)

        self.method = method
        self.url = url
        self.headers = headers
        self.files = files
        self.data = data
        self.json = json
        self.params = params
        self.auth = auth
        self.cookies = cookies
        self.base_url = base_url
        self.url_method = url_method
        self.url_data = url_data

    def method_new(self):
        self.base_url = config.BASE_URL
        s = Session()
        url = urljoin(self.base_url, '/'.join((self.url_method,) + self.url_data))
        print(url)
        req = Request(method=self.method.upper(), url=url, headers=self.headers,
                    files=self.files, data=self.data, params=self.params, auth=self.auth,
                    cookies=self.cookies, json=self.json)
        prepped = req.prepare()
        # 如果需要设置代理，可以在s.send中添加并进行配置, 详情查看send的源码
        resp = s.send(prepped)
        return resp

if __name__ == '__main__':
    pass