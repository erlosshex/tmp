# -*- coding: utf-8 -*-

class solution:
    def __init__(self,number,n=2,m=0):
        self.num=number
        self.flag_list=[(i+1,[True]) for i in range(number)]
        self.mod=n
        self.count=0;
        self.del_num=m-1
    def list_num(self):
        return len(self.flag_list)
    def inc_func(self):
        self.count=self.count+1
        self.count=self.count%self.mod
    def deal_func(self):
        self.flag_list=list(filter(lambda x: x[1][0]==True, self.flag_list))
    def solve(self):
        for item in self.flag_list:
            if item[1][0]==True:
                if self.count==self.del_num:
                    item[1][0]=False
                self.inc_func()

            else:
                continue
        #print("before --> ",self.flag_list)
        self.deal_func()
        #print("after --> ",self.flag_list)
    def result(self):
        while self.list_num()!=1:
            self.solve()
        return self.flag_list

if __name__=="__main__":
    a=solution(20,2)
    print(a.result())
