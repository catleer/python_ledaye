"""
Created by catleer on 2018-05-21.
"""
__author__ = 'catleer'

registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')

if __name__ == '__main__':
    f1()
    f2()
    f3()