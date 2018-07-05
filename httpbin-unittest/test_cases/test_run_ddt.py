"""
Created by catleer on 2018-05-21.
"""
__author__ = 'catleer'

import unittest, json
import sys
sys.path.append('.')
from common import get_casedata
from common import httpmethods
# from common import send_email
import ddt
import paramunittest
# 生成测试用例

cases = [case for case in get_casedata.get_case()]
case_data = [case for case in get_casedata.get_case_data()]


@ddt.ddt
class TestCases(unittest.TestCase):

    @ddt.data(*cases)
    def test_case(self, data):
        self.flag = data['Flag']
        self.case_module = data['CaseModule']
        self.case_id = data['CaseId']
        self.title = data['Title']
        self.desc = data['Desc']
        self.url_path = data['UrlPath']
        self.url_data = data['UrlData']
        self.http_data = data['HttpData']
        self.result = data['Result']

        h = httpmethods.Http(url_method=self.url_path, url_data=self.url_data, method=self.http_data['method'],
                             headers=self.http_data['headers'], data=self.http_data['data'],
                             params=self.http_data['params'], auth=self.http_data['auth'],
                             cookies=self.http_data['cookies'], hooks=self.http_data['hooks'], json=self.http_data['json'])

        r = h.method_new()
        # print(type(r.json()))
        # print(type(self.result['ResponseData']))
        self.assertEqual(r.status_code, self.result['StatusCode'])

        self.assertIn(json.dumps(self.result['ResponseData']), json.dumps(r.json()))


if __name__ == '__main__':
    # print(type(case_data[0][2]['ResponseData']))
    # print(len(case_data))
    unittest.main(verbosity=2)
