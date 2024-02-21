from typing import *

class Solution:
    def mergeSort(self,a:List[int],left:int,right:int)->list:
        if left>right: return [0]
        if left==right:
            return [a[left]]
        # chia 
        mid=(left+right)//2
        a1=self.mergeSort(a,left,mid)
        a2=self.mergeSort(a,mid+1,right)
        # tron
        length=len(a1)+len(a2)
        result=[0]*length
        i,i1,i2=0,0,0
        while i<length:
            if i1<len(a1) and i2<len(a2):
                if a1[i1]<=a2[i2]:
                    result[i]=a1[i1]
                    i+=1;i1+=1
                else:
                    result[i]=a2[i2]
                    i+=1;i2+=1
            else:
                if i1<len(a1):
                    result[i]=a1[i1]
                    i+=1;i1+=1
                else:
                    result[i]=a2[i2]
                    i+=1;i2+=1
        return result
                    
        
    def sortArray(self, a: List[int]) -> List[int]:
        return self.mergeSort(a,0,len(a)-1)
    
arr=[3,2,0]
s=Solution()
print(s.sortArray(arr))
