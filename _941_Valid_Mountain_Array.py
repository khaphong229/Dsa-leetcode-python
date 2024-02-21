from typing import *

class Solution:
    def validMountainArray(self, a: List[int]) -> bool:
        m=len(a)
        isCheck=True
        if m<3: return False
        for i in range(m-1):
            j=i+1
            if a[i]>a[j]:
                if isCheck==True:
                    if i==0: return False
                    isCheck=False
            elif a[i]<a[j]:
                if isCheck==False: return False
            else: return False
        if isCheck==False:
            return True
        return False

arr = [2,1]
s=Solution()
print(s.validMountainArray(arr))