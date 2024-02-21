from typing import *

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        arr=[str(i) for i in range(1,n+1)]
        new=sorted(arr)
        return list(map(int,new))

n = 13
s=Solution()
print(s.lexicalOrder(n))