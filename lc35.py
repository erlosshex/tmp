class Solution(object):
    def searchInsert(self,nums,target):
        if target in nums:
            return nums.index(target)
        i=0
        while(i<len(nums)):
            if nums[i]<=target:
                i+=1
            else:
                break
        return i
