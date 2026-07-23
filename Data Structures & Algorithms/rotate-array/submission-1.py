class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k% len(nums)
        def reverse(r, array: List[int],l = 0):
            while l < r:
                leftside = array[l]
                array[l] = array[r]
                array[r] = leftside
                l+=1
                r-=1
            return array

        nums = reverse(r = len(nums)-1, array= nums)
        nums = reverse(r = k-1, array = nums)
        nums = reverse(r = len(nums)-1, array = nums,l = k )
        return nums