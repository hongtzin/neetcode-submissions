class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        i = 0 
        r = 0 

        while r < len(t):
            if i == len(s):
                return True
            if s[i] == t[r]:
                i += 1
            
            r += 1
        if i == len(s):
                return True
        return False