from typing import *


class Solution:
    def findDisappearedNumbers(self, a: List[int]) -> List[int]:
        length = len(a)
        exists = [False] * (length + 1)
        for i in range(length):
            exists[a[i]] = True
        return [i for i in range(1, length + 1) if exists[i] == False]


arr = [1, 1]
print(Solution().findDisappearedNumbers(arr))
