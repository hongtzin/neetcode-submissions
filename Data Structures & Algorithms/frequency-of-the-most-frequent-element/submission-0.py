class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        sortednums = sorted(nums)

        l = 0 
        maxfreq = 0 
        opcount = 0

        for r in range(len(sortednums)): #iterate through each number in sortednums

            # each time we get to a new number we count the number of operations to make the sortednums[r] the most frequent element from l
            opcount += (r - l) * (sortednums[r] - sortednums[r-1]) 
            
            while l <= r and opcount > k:
                opcount -= sortednums[r] - sortednums[l]
                l += 1
            
            maxfreq = max(maxfreq, r - l + 1)
        
        return maxfreq

