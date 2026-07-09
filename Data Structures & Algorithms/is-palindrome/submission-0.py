class Solution:
    def isPalindrome(self, s: str) -> bool:
        startpointer = 0 
        endpointer = len(s) - 1

        while startpointer < endpointer:
            if not((ord(s[startpointer]) <= 122 and ord(s[startpointer]) >= 97) or (ord(s[startpointer]) <= 90 and ord(s[startpointer]) >= 65) or s[startpointer].isdigit()):
                startpointer +=1
                continue
            if not((ord(s[endpointer]) <= 122 and ord(s[endpointer]) >= 97) or (ord(s[endpointer]) <= 90 and ord(s[endpointer]) >= 65) or s[endpointer].isdigit()):
                endpointer -=1
                continue        
            if ord(s[startpointer].lower()) != ord(s[endpointer].lower()):
                return False
            
            startpointer += 1 
            endpointer -=1
        return True
