from typing import *

class Solution:
    def fib(self, n: int) -> int:
        temp=[0]*(n+1)
        temp[n]
        if n<2: return n
        return self.fib(n-1)+self.fib(n-2)

n=4
print(Solution().fib(n))