class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        hm = {"(": ")", "[":"]", "{":"}"}
        stack = []
        for char in s:
            if char in hm.keys():
                stack.append(char)
            elif char in hm.values():
                if len(stack) == 0:
                    return False
                corresp = stack.pop()
                if char != hm[corresp]:
                    return False
            else:
                return False
        if len(stack) != 0:
            return False
                
        return True
            