from typing import *

class Solution:
    def binary1(self,a:List[int],x:int)->int:
        length=len(a)
        left=0
        right=length-1
        while (left<=right):
            mid=(left+right)//2
            if x==a[mid]: return mid
            elif x>a[mid]: left=mid+1
            else: right=mid-1
        return -1

    
    def binary2(self,a:List[int],x:int,left:int,right:int)->int:
        if left>right: return -1
        mid=(left+right)//2
        if x==a[mid]: return mid
        elif x>a[mid]: self.binary2(a,x,mid+1,right)
        else: self.binary2(a,x,left,mid-1)
        

arr=[1,2,3,4,5,3,12]    
s=Solution()
print(s.binary2(arr,1,0,len(arr)-1))

        