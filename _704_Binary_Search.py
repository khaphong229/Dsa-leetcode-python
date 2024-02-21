from typing import *

class Solution:
    def bSearch(self,a:List[int],x:int,left:int,right:int)->int:
        if left>right:
            return -1
        mid=(left+right)//2
        if a[mid]==x:
            return mid
        elif a[mid]>x:
            return self.bSearch(a,x,left,right-1)
        else:
            return self.bSearch(a,x,left+1,right)
    def search(self, a: List[int], x: int) -> int:
        length=len(a)
        return self.bSearch(a,x,0,len(a)-1)
        
arr=[-1,0,3,5,9,12]
target=0
s=Solution()
print(s.search(arr,target))