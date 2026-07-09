class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkvalidPalindrome(left:int, right:int,s: str) ->bool:
            l,r =left,right
            while l <= r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        l,r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                break
            l+=1
            r-=1
        if r < l:
            return True
        print(l,r)
        # print(checkvalidPalindrome(l+1,r,s), checkvalidPalindrome(l,r-1,s))    
        if checkvalidPalindrome(l+1,r,s) or checkvalidPalindrome(l,r-1,s):
            return True
        return False