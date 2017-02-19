# coding: utf-8
'''
fin=open("data.txt")
data=fin.read()
fin.close()

fout=open("out1.txt","w")
fout.write(data)
fout.close()
'''

import sys
fin=sys.stdin

fout=open("out1.txt","a")
data=fin.read()
fout.write(data)
fout.close()
