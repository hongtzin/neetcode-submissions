class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        streak = 0
        for num in nums:
            beforenum = num - 1
            if beforenum not in hs:
                numstreak = 0
                currentnum = num
                while currentnum in hs:
                    numstreak +=1
                    currentnum +=1

                if numstreak > streak:
                    streak = numstreak
        return streak