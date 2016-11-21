'''
-- first test

def func1():
    x=1
    print globals()
    print
    print 'before func1: ',locals()
    print

    def func2():
        a=1
        print 'before func2: ',locals()
        print
        a+=x
        print 'after func2: ', locals()
        print

    func2()
    print 'after func1: ',locals()
    print
    print globals()
    print


if __name__=='__main__':
    func1()
'''

'''
-- second test

def func1():
    x=1
    print globals()
    print
    print 'before func1: ',locals()
    print

    def func2():
        a=1
        print 'before func2: ',locals()
        print
        x+=x
        print 'after func2: ', locals()
        print

    func2()
    print 'after func1: ',locals()
    print
    print globals()
    print


if __name__=='__main__':
    func1()
'''

import copy
from copy import deepcopy

def func():
    x=123
    print 'func locals: ',locals()

s='hello world'

if __name__=='__main__':
    func()
    print 'globals: ',globals()
