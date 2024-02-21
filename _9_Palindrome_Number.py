from typing import *


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]


x = 10
s = Solution()
print(s.isPalindrome(x))
