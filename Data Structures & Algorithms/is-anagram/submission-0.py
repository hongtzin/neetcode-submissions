class Solution:
    def isAnagram(self,s: str, t: str) -> bool:
        shm = {}
        thm = {}
        for char in s:
            if char not in shm:
                shm[char] = 0
            shm[char] += 1 
        for char in t:
            if char not in thm:
                thm[char] = 0
            thm[char] += 1 
        
        if len(shm) != len(thm):
            return False
        
        for key,value in shm.items():
            if key not in thm or value!= thm[key]:
                return False

        return True