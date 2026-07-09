class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        minele = nums[r]
        
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] < nums[r] : 
                r = mid
                minele = min(minele, nums[mid])
            else:
                l = mid + 1
        return minele
