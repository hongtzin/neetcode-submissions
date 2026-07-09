from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for index, num in enumerate(nums):
            addtwo = target - num
            if addtwo in hm:
                return [index, hm[addtwo]] if index < hm[addtwo] else [hm[addtwo],index]
            hm[num] = index

        