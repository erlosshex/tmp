# coding:utf-8

def is_equal(answer,num):
    if answer<num:
        print 'too small!'
        return False
    elif answer>num:
        print 'too big!'
        return False
    else:
        print 'BINGO!'
        return True

from random import randint

num=randint(1,101)
bingo=False

while bingo==False:
    answer=input('Guess ')
    bingo=is_equal(answer,num)
