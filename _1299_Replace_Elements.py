from typing import *

class Solution:
    def replaceElements(self, a: List[int]) -> List[int]:
        length=len(a)
        for i in range(length-1,-1,-1):
            if i!=length-1:
                a[i]=max(a[i],a[i+1])
        for i in range(1,length):
            a[i-1]=a[i]
        a[length-1]=-1
        return a

arr = [17,18,5,4,6,1]
s=Solution()
print(s.replaceElements(arr))