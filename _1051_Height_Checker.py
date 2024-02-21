from typing import *


class Solution:
    def heightChecker(self, a: List[int]) -> int:
        length = len(a)
        res = [0] * length
        for i in range(length):
            res[i] = a[i]
        count = 0
        # for i in range(length):
        #     minIndex=i
        #     for j in range(i+1,length):
        #         if a[j]<a[minIndex]:
        #             minIndex=j
        #     if minIndex!=i:
        #         temp=a[minIndex]
        #         a[minIndex]=a[i]
        #         a[i]=temp
        a.sort()
        for i in range(length):
            if a[i] != res[i]:
                count += 1
        return count


arr = [1, 1, 4, 2, 1, 3]
s = Solution()
print(s.heightChecker(arr))
