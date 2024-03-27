from typing import *

class Solution:
    def __init__(self) -> None:
        self.temp=[0]*31
    # def fib(self, n: int) -> int:
    #     if n<2: return n
    #     if n in self.temp:
    #         return self.temp[n]
    #     else:
    #         self.temp[n] =  self.fib(n-1)+self.fib(n-2)
    #     return self.temp[n]
    
    def fib(self, n: int) -> int:
        self.temp[0]=0
        self.temp[1]=1
        for i in range(2,31):
            self.temp[i]=self.temp[i-1]+self.temp[i-2]
        return self.temp[n]

n=10
print(Solution().fib(n))