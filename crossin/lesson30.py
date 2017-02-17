# coding:utf-8

word='helloworld'

for c in word:
    print c

print word[0]
print word[-2]

#word[1]='a'
print word[5:7]
print word[:-5]
print word[:]

newword=','.join(word)
