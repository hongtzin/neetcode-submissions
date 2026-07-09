class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l = 0 
        res = 0
        tcount = {}
        scount = {}
        lindex, rindex = -1,-1
        minlength = 1001
        for char in t:
            tcount[char] = tcount.get(char, 0) + 1
        # print(tcount)
        for r in range(len(s)):
            print(l, r)
            scount[s[r]] = scount.get(s[r], 0) + 1
            isValid = False
            while all(key in scount and scount[key] >= tcount[key] for key in tcount.keys()): # while the sliding window is not minimum length
                scount[s[l]] -=1
                l +=1
                isValid = True
            # print(l, r)
            if (r - l +2) < minlength and isValid:
                minlength = r - l + 2
                lindex,rindex = l-1,r
                print(minlength, lindex, rindex)
        if lindex == -1 and rindex == -1:
            return ""
        else:
            return s[lindex: rindex +1]