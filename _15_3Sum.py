from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        length=len(nums)
        nums.sort()
        for i in range(length-2):
            res=[]
            x=nums[i]
            j=i+1
            k=length-1
            while j<k:
                total=x+nums[j]+nums[k]
                if total==0:
                    ans.add((x,nums[j],nums[k]))
                    j+=1
                elif total<0:
                    j+=1
                else:
                    k-=1
        return ans
            
    
nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))