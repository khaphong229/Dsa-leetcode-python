from typing import *
class Solution:
    def partition(self,a:List[int],left:int,right:int,key:int)->int:
        iL=left
        iR=right
        while iL<=iR:
            while a[iL]<key: iL+=1
            while a[iR]>key: iR-=1
            if iL<=iR:
                temp=a[iL]
                a[iL]=a[iR]
                a[iR]=temp
                iL+=1;iR-=1
        return iL
    
    def quick_sort(self,a:List[int],left:int,right:int)->None:
        if left>=right:
            return
        # choose key
        key=a[(left+right)//2]
        # partition array
        k=self.partition(a,left,right,key)
        #
        self.quick_sort(a,left,k-1)
        self.quick_sort(a,k,right)
        
        
    def main(self,a:List[int])->list:
        self.quick_sort(a,0,len(a)-1)
        return a

arr=[999,234,2,4,5,2]
s=Solution()
print(s.main(arr))