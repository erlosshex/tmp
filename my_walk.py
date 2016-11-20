#! /usr/bin/env python

'''
import os

line=os.sys.argv

if len(line)==1:
    my_path='.'
elif len(line)==2:
    my_path=argv[1]
else:
    print "Wrong Input"
    exit(0)
'''

def print_this_dir(tmp_path,seq=' ',depth=0):
    for i in os.listdir(tmp_path):
        print seq*depth,
        print i


def print_all_dir(cur_path,seq=' ',depth=0):
    for i in os.listdir(cur_path):
        now_path=os.path.join(cur_path,i)
        
        if os.path.isdir(now_path):
            print seq*depth*4+'+'+i+'/'
            
            print_all_dir(now_path+'/',seq,depth+1)
        elif os.path.isfile(now_path):
            print seq*depth*4+'-'+i

def print_dir(root_path):
    print '****************'
    print '~ --> root path'
    print '+ --> directory'
    print '- --> file'
    print '****************'
    print '\n'
    
    if os.path.isdir(root_path):
        print '~+'+root_path+'/'
        print_all_dir(root_path,' ',1)
    elif os.path.isfile(root_path):
        print '~-'+root_path
    else:
        print 'No such file or directory!'

if __name__=='__main__':
    import os
    tmp_path=raw_input("Please input: ")
    print_dir(tmp_path)
