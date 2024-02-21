from typing import *

class Solution:
    def containsDuplicate(self, a: List[int]) -> bool:
        return len(set(a))!=len(a)
nums = [1,1,1,3,3,4,3,2,4,2]
print(Solution().containsDuplicate(nums))
                