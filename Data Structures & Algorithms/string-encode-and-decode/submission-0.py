class Solution:

    def encode(self,strs: list[str]) -> str:
        encoded = ""
        for string in strs:
            stringlen = len(string)
            encoded += str(stringlen)
            encoded += "#"
            encoded += string
        return encoded

    def decode(self, s: str) -> list[str]:
        index = 0 
        slength = len(s)
        res = []
        while index < len(s):
            strlength = ""
            while s[index].isdigit():
                strlength += s[index]
                index += 1
            # print(index)
            strlength = int(strlength)
            
            index += 1 # to skip the separator, I think the separator actually doesnt matter what it is, can even be 'a', as long as it isnt a digit/number.
            # print(index)
            string = ""
            for i in range(strlength):
                string += s[index]
                index += 1
            # print(index)
            # print(string)
            # print(strlength)
            # print()    
            res.append(string)
        return res