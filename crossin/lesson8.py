# coding:utf-8
'''
a=1
while a!=0:
    print 'please input'
    a=input()
print 'over'
'''


num=10
print 'Guess what I think?'
bingo=False

while bingo==False:
    answer=input()

    if answer<num:
        print 'too small!'
    if answer>num:
        print 'too big!'
    if answer==num:
        print 'BINGO!'
        bingo=True
