from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_val=float('-inf')
        while left<right:
            calcul=(min(height[left],height[right]))*(right-left)
            max_val=max(max_val,calcul)
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        return max_val

height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))