def testif(num):
    if num%2==0 or num%3==0 or num%5==0:
        return True
    else:
        return False

test=[i for i in range(1,101) if testif(i)]

print ';'.join(map(str,test))
