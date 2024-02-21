from typing import *


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        temp = 0
        if n < 0:
            temp = -(n / 2) if n % 2 == 0 else (-n - 1) / 2
            x = 1 / x
        else:
            temp = n / 2 if n % 2 == 0 else (n - 1) / 2

        res = self.myPow(x, temp)

        return res**2 if n % 2 == 0 else x * res * res


x = float(input())
n = int(input())
s = Solution()
print(s.myPow(x, n))
