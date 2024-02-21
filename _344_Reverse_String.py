from typing import *


class Solution:
    def swap(self, a: List[str], i: int, j: int) -> None:
        if i < j:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            self.swap(a, i + 1, j - 1)

    def reverseString(self, s: List[str]) -> None:
        self.swap(s, 0, len(s) - 1)


arr = ["o", "l", "l", "e", "h"]
s = Solution()
s.reverseString(arr)
print(arr)
