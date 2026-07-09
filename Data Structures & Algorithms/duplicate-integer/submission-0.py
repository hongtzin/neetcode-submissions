class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniquevalues = set()

        for num in nums: 
            if num in uniquevalues:
                return True    
            uniquevalues.add(num)

        return False