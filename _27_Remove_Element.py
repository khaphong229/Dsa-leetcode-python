from typing import List

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         length=len(nums)
#         i=0
#         while i<length:
#             if nums[i]==val:
#                 for j in range(i,length-1):
#                     nums[j]=nums[j+1]
#                 length-=1
#             else:
#                 i+=1
#         return length


# optimize code
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
s = Solution()
print(s.removeElement(nums, val))
