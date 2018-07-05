"""
Created by catleer on 2018-05-21.
"""
__author__ = 'catleer'

"""
@decorate
def target():
    print('running target')
    
两者效果一致：
def target():
    print('running target')
target = decorate(target())
"""

def deco(func):
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print('running target()')
"""
1、deco返回inner函数对象
2、使用deco装饰target
3、调用被装饰的target会运行inner
4、审查对象，发现target是inner的引用
"""