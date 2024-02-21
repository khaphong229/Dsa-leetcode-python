from typing import *

class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        j=1
        for i in range(1,len(arr)):
            if arr[i-1]!=arr[i]:
                arr[j]=arr[i]
                j+=1
        return j


arr=[1,1,2]
s=Solution()
print(s.removeDuplicates(arr))
