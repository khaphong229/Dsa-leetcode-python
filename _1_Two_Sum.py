from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''length_list=len(nums)
        for i in range(length_list):
            for j in range(i+1,length_list):
                if nums[i]+nums[j]==target:
                    return [i,j]'''
        numMap=dict({})
        length=len(nums)
        for i in range(length):
            complement=target-nums[i]
            if complement in numMap:
                return [numMap[complement],i]
            numMap[nums[i]]=i
        return []
        
        
nums = [2,7,11,15]
target = 9
result = Solution().twoSum(nums,target)
print(result)