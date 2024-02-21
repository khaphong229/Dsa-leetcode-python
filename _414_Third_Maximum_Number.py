from typing import *
class Solution:
    def insert(self,a:List[int],x:int)->list:
        length=len(a)
        i=0
        while i<length:
            if a[i]==x:
                return
            elif x>a[i]:
                break
            else:
                i+=1
        if i<length:
            for j in range(length-2,i-1,-1):
                a[j+1]=a[j]
            a[i]=x
        return a
    def thirdMax(self, a: List[int]) -> int:
        length=len(a)
        max_arr=[float('-inf')]*3
        for i in range(length):
            max_arr=self.insert(max_arr,a[i])
        if max_arr[2]==float('-inf'):
            return max_arr[0]
        else:
            return max_arr[2]
            

arr=[1,2]
s=Solution()
print(s.thirdMax(arr))