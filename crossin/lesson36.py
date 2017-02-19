# coding: utf-8

try:
    f=file('non-exist.txt')
    print 'file opened!'
    f.close()

except:
    print 'file not exists.'

print 'Done'
