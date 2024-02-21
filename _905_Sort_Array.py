from typing import *
# class Solution:
#     def sortArrayByParity(self, a: List[int]) -> List[int]:
#         length=len(a)
#         j=0
#         for i in range(length):
#             if a[i]%2==0:
#                 a[i],a[j]=a[j],a[i]
#                 j+=1
#         return a
    
# class Solution:
#     def sortArrayByParity(self, a: List[int]) -> List[int]:
#         length=len(a)
#         even=[a[i] for i in range(length) if a[i]%2==0]
#         odd=[a[i] for i in range(length) if a[i]%2==1]
#         new=even+odd
#         return new

class Solution:
    def sortArrayByParity(self, a: List[int]) -> List[int]:
        i=0
        j=len(a)-1
        while i<j:
            if a[i]%2!=0:
                if a[j]%2==0:
                    if i<j:
                        a[i],a[j]=a[j],a[i]
                else:
                    j-=1
            else:
                i+=1
        return a

nums = [3,1,2,4]
s=Solution()
print(s.sortArrayByParity(nums))