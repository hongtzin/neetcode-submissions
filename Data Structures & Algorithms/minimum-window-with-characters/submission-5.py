class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l = 0 
        res = 0
        tuniqcount = {}
        scount = {}
        minlength = 1001
        lindex,rindex = -1,-1

        for char in t: 
            tuniqcount[char] = tuniqcount.get(char,0) + 1
        tuniqflag = {}
        for key in tuniqcount.keys():
            tuniqflag[key] = False
        # print(tuniqcount,tuniqflag)

        have = 0 
        need = len(tuniqflag)
        tuniqkeys = tuniqcount.keys()

        for r in range(len(s)):
            scount[s[r]] = scount.get(s[r], 0) + 1
            if s[r] in tuniqkeys and scount[s[r]] >= tuniqcount[s[r]] and not tuniqflag[s[r]]:
                have += 1
                tuniqflag[s[r]] = True

            while need == have:
                scount[s[l]] -= 1
                if s[l] in tuniqkeys and scount[s[l]] < tuniqcount[s[l]]:
                    have -=1
                    tuniqflag[s[l]] = False
                    if (r - l + 1) < minlength:
                        minlength = r - l + 1
                        lindex = l 
                        rindex = r
                l+=1

        if lindex == -1 and rindex == -1:
            return ""
        return s[lindex: rindex +1]

