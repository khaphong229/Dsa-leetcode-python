from typing import *

class Solution:
    def containsDuplicate(self, a: List[int]) -> bool:
        hashes=set()
        for num in a:
            if num in hashes:
                return True
            hashes.add(num)
        return False
    
nums = [1,1,1,3,3,4,3,2,4,2]
print(Solution().containsDuplicate(nums))
                