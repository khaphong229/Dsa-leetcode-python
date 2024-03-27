from typing import *

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''length=len(nums)
        new_nums=[0]*length
        for i in range(length):
            pre_nums=nums[:i]
            post_nums=nums[i+1:]
            total_nums=pre_nums+post_nums
            ans=1
            for j in total_nums:
                ans*=j
            new_nums[i]=ans
        return new_nums'''
        
        '''res=[1]*(len(nums))
        prefix=1
        for i in range(len(nums)):
            res[i]*=prefix
            prefix*=nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res'''
        
        length=len(nums)
        pre_nums=[0]*length
        post_nums=[0]*length
        pre_val=1
        post_val=1
        for i in range(length):
            j=-1-i
            pre_nums[i]=pre_val
            post_nums[j]=post_val
            pre_val*=nums[i]
            post_val*=nums[j]
        return [pre*post for pre, post in zip(pre_nums,post_nums)]
nums = [1,2,3,4]
print(Solution().productExceptSelf(nums))
