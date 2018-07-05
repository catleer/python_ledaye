"""
Created by catleer on 2018-05-21.
"""
__author__ = 'catleer'

import sys
sys.path.append('.')

import unittest

from test_cases import test_run_ddt

# 生成测试集
def all_test():
    suite1 = unittest.TestLoader().loadTestsFromModule('test_run_ddt')
    alltests = unittest.TestSuite([suite1])
    return alltests

if __name__ == '__main__':
    print(all_test())

