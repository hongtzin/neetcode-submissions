from collections import defaultdict
class Solution:
    def groupAnagrams(self,strs: list[str]) -> list[list[str]]:
        count = defaultdict(list)
        for str in strs:
            key = [0] * 26    
            for char in str:
                key[ord(char) - ord('a')] += 1 
            count[tuple(key)].append(str) ## you should convert it to tuple because keys cant be mutable in hashmaps.
        return list(count.values())
    