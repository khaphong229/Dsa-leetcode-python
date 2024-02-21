from typing import *
class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
        length=len(arr)
        check=False
        for i in range(length):
            if arr[i]==target:
                check=True
                return i
            else:
                if check==False:
                    