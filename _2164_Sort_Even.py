from typing import List

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        length=len(nums)
        print(nums[0::2])
        even=sorted([nums[i] for i in range(length) if i%2==0])
        odd=sorted([nums[i] for i in range(length) if i%2==1],reverse=True)
        even_idx=0
        odd_idx=0
        for i in range(length):
            if i%2==0:
                nums[i]=even[even_idx]
                even_idx+=1
            else:
                nums[i]=odd[odd_idx]
                odd_idx+=1
        return nums
    
nums = [4,1,2,3]
print(Solution().sortEvenOdd(nums))