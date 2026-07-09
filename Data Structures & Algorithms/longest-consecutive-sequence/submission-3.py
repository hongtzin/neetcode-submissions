class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniquenums = set(nums)
        maxC = 1 
        if len(nums) == 0:
            return 0
            
        for num in nums:
            if num - 1 not in nums:
                size = 1
                plh = num + 1
                while plh in nums:
                    size += 1
                    plh += 1
                     
                maxC = max(size, maxC)
        return maxC

