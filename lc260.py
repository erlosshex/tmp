class Solution(object):
    def singleNumber(self,nums):
        if len(nums)==0:
            return []
        res_dict={}
        res_list=[]
        for i in nums:
            if i in res_dict:
                res_dict[i]+=1
            else:
                res_dict[i]=1
        for i in res_dict:
            if res_dict[i]==1:
                res_list.append(i)
        return res_list

if __name__=='__main__':
    a=Solution()
    import sys
    data_num=sys.stdin.readline()
    data_num=map(int,data_num[1:len(data_num)-2].split(','))
    print a.singleNumber(data_num)
