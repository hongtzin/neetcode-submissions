class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1count = {}
        
        for i in range(len(s1)):
            s1count[s1[i]] = s1count.get(s1[i], 0) + 1
    
        l = 0
        s2count = {} 
        have = 0 
        need = len(s1count)

        for r in range(len(s2)): # sliding r to the right
            s2count[s2[r]] = s2count.get(s2[r],0) + 1 # add the freq count to 

            if s2[r] in s1count and s2count[s2[r]] == s1count[s2[r]]: # if s2[r] is in s1count and the freq 
                have += 1
            
            while have == need: #so long it is a valid window 
                s2count[s2[l]] -= 1
                if s2[l] in s1count and s2count[s2[l]] < s1count[s2[l]]: # if s2[l] is in s1count and the freq of s2[l] in s2count is lower than that in s1count
                    have -=1
                    if (r - l + 1) == len(s1):
                        return True
                print(l,r)
                l+=1 
        return False