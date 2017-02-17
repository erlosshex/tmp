# coding: utf-8

from random import randint

num=randint(1,101)
bingo=False

def is_equal(answer,num):
    if answer<num:
        print 'too small!'
        return False
    if answer>num:
        print 'too big!'
        return False
    if answer==num:
        print 'BINGO!'
        return True

while bingo==False:
    answer=input('Guess ')
    bingo=is_equal(answer,num)
