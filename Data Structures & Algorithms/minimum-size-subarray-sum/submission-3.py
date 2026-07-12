class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 
        total = 0 
        minl = 100001
        for r in range(len(nums)):
            total += nums[r]
            if total >= target:
                print(l,r)
                while total >= target:
                    total -= nums[l]
                    l += 1
                print(l,r)
                minl = min(minl, r - l + 2)
                print(minl)
            print(total)
            print()

        if minl > 100000:
            return 0
        return minl

