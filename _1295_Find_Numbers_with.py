from typing import List
class Solution:
    def amount_of_numbers(self,num: int)-> int:
        count_1=0
        while num!=0:
            num//=10
            count_1+=1
        return count_1

    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            if self.amount_of_numbers(i)%2==0:
                count+=1
        return count

    def __str__(self,arr: List[int])->int:
        result=self.findNumbers(arr)
        return result

arr=[12,345,2,6,7896]
s=Solution()
print(s.__str__(arr))
