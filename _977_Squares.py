from typing import *
class Solution:
    def sortedSquares(self, a: List[int]) -> List[int]:
        length=len(a)
        for i in range(length):
            a[i]=a[i]**2
        # for i in range(length):
        #     minIndex=i
        #     for j in range(i+1,length):
        #         if a[j]<a[minIndex]: minIndex=j
        #     if minIndex!=i:
        #         temp=a[i]
        #         a[i]=a[minIndex]
        #         a[minIndex]=temp
        return sorted(a)

arr=[-4,-1,0,3,10]
s=Solution()
print(s.sortedSquares(arr))