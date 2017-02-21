def func():
    global x
    print 'x beginning of func(): ',x
    x=2
    print 'x ending of func(): ',x


x=50
func()
print 'x after calling func(): ',x
