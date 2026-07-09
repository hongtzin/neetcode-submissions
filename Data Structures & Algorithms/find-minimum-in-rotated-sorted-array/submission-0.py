class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0 
        high = len(nums)-1
        min = nums[0] 

        while low <= high:
            # print(low, high)
            mid = low + (high - low) // 2
            # print(mid)
            # print(min)
            # if nums[mid] == min:
            #     print("early termination")
            #     return min
            if nums[mid] < min:
                
                min = nums[mid]
                high = mid - 1
                
            else:
                low = mid + 1
            # print()
            
        return min