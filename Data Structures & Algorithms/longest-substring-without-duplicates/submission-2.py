class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        res = 0
        hs = set()
        for i in range(len(s)):
            if s[i] in hs:
                while s[i] in hs:
                    print(l)
                    hs.remove(s[l])
                    l+=1
                    

            res = max(res, i-l+1)
            hs.add(s[i])
        return res