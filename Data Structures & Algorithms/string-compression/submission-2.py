class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        r = 1 
        s = ""
        while r < len(chars):
            if chars[r] != chars[r-1]:
                if r - l == 1:
                    s += chars[l]
                else:
                    s += chars[l]
                    s += str(r-l)
                    
                l = r
            r+=1
        if r - l == 1:
            s += chars[l]
        else:
            s += chars[l]
            s += str(r-l)
        for i in range(len(s)):
            chars[i] = s[i]

        return len(s)