from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        sort_strs=[''.join(sorted(word)) for word in strs]
        dict_strs=dict({})
        for index, value in enumerate(sort_strs):
            if value not in dict_strs:
                dict_strs[value]=[strs[index]]
            else:
                dict_strs[value].append(strs[index])
        for index, value in dict_strs.items():
            ans.append(sorted(value))
        return sorted(ans, key=len)
        

strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))