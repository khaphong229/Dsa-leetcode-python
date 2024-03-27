from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freMap=dict({})
        for i in nums:
            if i in freMap:
                freMap[i]+=1
            else:
                freMap[i]=1
        result=sorted(list(freMap.items()),key=lambda x:-x[1])
        return [result[i][0] for i in range(k)]
nums = [1,1,1,2,3,4]
k = 2
print(Solution().topKFrequent(nums,2))