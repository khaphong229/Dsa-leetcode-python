from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        maxLength, currentLength = 1, 1
        length=len(nums)
        for i in range(1,length):
            if nums[i]!=nums[i-1]:
                if nums[i]-nums[i-1]==1:
                    currentLength+=1
                else:
                    currentLength=1
            maxLength=max(maxLength,currentLength)
        return maxLength


nums = [100, 4, 200, 1, 3, 2]
print(Solution().longestConsecutive(nums))
