from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_profit=prices[0]
        length=len(prices)
        for i in range(1,length):
            max_profit=max(max_profit,(prices[i]-min_profit))
            min_profit=min(min_profit,prices[i])
        return max_profit
prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))