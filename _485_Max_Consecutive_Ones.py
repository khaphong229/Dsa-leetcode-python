from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, a: List[int]) -> int:
        maxCount=0
        fre=0
        for i in a:
            if i==0: fre=0
            else:
                fre+=1
                if fre>maxCount: maxCount=fre
        return maxCount
                
arr=[0]
s=Solution()
print(s.findMaxConsecutiveOnes(arr))
