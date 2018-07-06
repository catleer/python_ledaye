"""
Created by catleer on 2018-05-21.
"""
import os

__author__ = 'catleer'

import sys
sys.path.append('.')

from unittest import TestLoader, TestSuite, TextTestRunner

from test_cases import test_run_ddt, test_run_param

# 生成测试集
def all_test():
    suit1 = TestLoader().loadTestsFromModule(test_run_ddt)
    suit2 = TestLoader().loadTestsFromModule(test_run_param)
    suites = TestSuite([suit1, suit2])
    return suites

# discover生成测试集
def all_discover_test():
    test_dir = os.getcwd() + r'\test_cases'
    # print(test_dir)
    suites = TestLoader().discover(start_dir=test_dir, pattern="test_*.py")
    return suites

# 生成测试报告的方式
def report():
    pass

if __name__ == '__main__':
    print(os.getcwd())
    print(os.path.join(os.getcwd(), 'test_cases'))
    """
    HtmlTestRunner应该是重写了TextTestRunner
    """
    # with open('log.txt', 'w') as f:
    #     runner = TextTestRunner(stream=f)
    #     result = runner.run(all_discover_test())

    import HTMLTestRunner
    report_dir = os.path.join(os.getcwd(), 'reports')
    with open(report_dir+r'/result.html', 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               title="学习测试报告输出",
                                               description="测试报告输出的具体内容")
        runner.run(all_discover_test())
