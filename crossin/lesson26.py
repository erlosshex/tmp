# coding: utf-8

l=[365,'everyday',0.618,True]

print l[1]

print l
l[0]=123
print l

l.append(1024)
print l

del l[0]
print l

from random import choice

print 'Choose one side to shoot:'
print 'left, center, right'
you=raw_input()
print 'You kicked'+you
direction=['left','center','right']
com=choice(direction)
print 'Computer saved' + com
if you!=com:
    print "Goal!"
else:
    print "Oops..."
