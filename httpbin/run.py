"""
Created by catleer on 2018-05-21.
"""
__author__ = 'catleer'

import re
from urllib.parse import urljoin

import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
import pytest


# url = 'http://192.168.86.131:8088/'

methods = ['GET', 'POST', 'PATCH', 'DELETE', 'PUT']
method = methods[1]
interface = ['HTTP methods', 'Auth', 'Status Codes', 'Requests Inspection',
             'Response Inspection', 'Response Formats', 'Dynamic data',
             'Cookies', 'Images', 'Redirects', 'Anything']


class TestHttpMethods:

    @classmethod
    def setup_class(cls):
        cls.url = 'http://192.168.86.131:8088/'
        cls.data = {'haha': 'nihao'}

    def test_get(self):
        url = urljoin(self.url, 'get')
        r = requests.get(url, params=self.data).json()
        print(r)
        # assert r['url'] == url
        assert r['args'] == self.data

    def test_post(self):
        url = urljoin(self.url, 'post')
        r = requests.post(url, data=self.data).json()
        assert r['url'] == url
        assert r['form'] == self.data

    def test_patch(self):
        url = urljoin(self.url, 'patch')
        r = requests.patch(url, data=self.data).json()
        assert r['url'] == url
        assert r['form'] == self.data

    def test_put(self):
        url = urljoin(self.url, 'put')
        r = requests.put(url, data=self.data).json()
        assert r['url'] == url
        assert r['form'] == self.data

    def test_delete(self):
        url = urljoin(self.url, 'delete')
        r = requests.delete(url, data=self.data).json()
        assert r['url'] == url
        assert r['form'] == self.data

class TestAuth:
    @classmethod
    def setup_class(cls):
        cls.url = 'http://192.168.86.131:8088/'
        # cls.data = {'haha': 'nihao'}

    def test_basicauth_y(self):
        data = 'aa', '123'
        url = urljoin(self.url, '/'.join(('basic-auth',) + data))
        print(data)
        r = requests.get(url, auth=(data)).json()
        print(r)
        assert r['user'] == data[0]

    def test_basicauth_n(self):
        data = ('aa', '123')
        url = urljoin(self.url, '/'.join(('basic-auth',) + data))
        r = requests.get(url, auth=('aa', 'bb'))
        assert r.status_code == 401

    def test_bearer_y(self):
        headers = {'Authorization': 'justtestauth'}
        url = urljoin(self.url, 'bearer')
        r = requests.get(url, headers=headers)
        assert r.status_code == 200
        r = r.json()
        assert r['token'] == headers['Authorization']

    def test_bearer_n(self):
        headers = {}
        url = urljoin(self.url, 'bearer')
        r = requests.get(url, headers=headers)
        assert r.status_code == 401

    def test_digest_auth_y(self):
        data = ('auth-int', 'testu', 'testp')
        inter_path = ('diges-auth')
        url = urljoin(self.url, '/'.join(inter_path+data))
        r = requests.get(url, auth=data)
        assert r.status_code == 200
        r = r.json()
        # assert r['']
