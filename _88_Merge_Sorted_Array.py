from typing import List

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         for i in nums2:
#             self.solve(nums1,m,i)
#             m+=1
#     def solve(self,a: List[int],m: int,x: int)-> list:
#         check=False
#         for k in range(m):
#             if a[k]>x:
#                 check = True
#                 for i in range(m-1,k-1,-1):
#                     a[i+1]=a[i]
#                 a[k]=x
#                 break
#         if check==False:
#             a[m]=x

#optimize code

class Solution:
    def merge(self, a: List[int], m: int, b: List[int], n: int) -> None:
        i,j,k=m-1,n-1,(m+n)-1
        while k>=0:
            if j<0:a[k]=a[i];i-=1
            elif i<0:a[k]=b[j];j-=1
            elif a[i]>b[j]:a[k]=a[i];i-=1
            else:a[k]=b[j];j-=1
            k-=1
        return a

a=[1,2,3,0,0,0]
m=3
b=[2,5,6]
n=3
s=Solution()
print(s.merge(a,m,b,n))
