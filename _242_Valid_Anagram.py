class Solution(object):
    def isAnagram(self, s, t):
        # return sorted(s)==sorted(t)
        if len(s)!=len(t): return False
        a,b=dict({}),dict({})
        for i in s:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        for i in t:
            if i in b:
                b[i]+=1
            else:
                b[i]=1
        for key in a:
            if key not in b: 
                return False
            if a[key]!=b[key]:
                return False
        return True
    
s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s,t))