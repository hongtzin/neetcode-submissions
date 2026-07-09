class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        res = 0
        hm = {}

        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r],0) + 1
            while (r - l + 1) - max(hm.values()) > k: # if the sliding window is invalid
                hm[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res