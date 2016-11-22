def myPow(x,n):
    if n==1:
        return x
    if n%2==1:
        return x*myPow(x*x,int(n/2))
    else:
        return myPow(x*x,int(n/2))


if __name__=='__main__':
    print 'POW(2,3) --> ',myPow(2,3)
    print 'POW(17,43) --> ',myPow(17,43)
    print 'POW(7,8) --> ',myPow(7,8)
