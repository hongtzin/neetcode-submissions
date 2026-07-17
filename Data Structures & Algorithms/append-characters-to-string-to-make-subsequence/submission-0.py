class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0 
        r = 0 
        # characters = 0 

        while r < len(s):
            if i == len(t):
                return 0
            if t[i] == s[r]:
                i += 1

            r+=1
        return len(t) - i
