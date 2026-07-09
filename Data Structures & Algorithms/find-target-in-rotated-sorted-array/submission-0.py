class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        minindex = left
        # return minindex

        left1 = 0
        right1 = minindex - 1

        while left1 <= right1:
            mid1 = (left1 + right1) // 2
            # print(mid1)
            if nums[mid1] == target:
                # print(mid1)
                return mid1
            elif nums[mid1] > target:
                right1 = mid1 -1
                print("right1: " + str(right1))
            else:
                left1 = mid1 + 1
                print("left1: " + str(left1))

        left2 = minindex
        right2 = len(nums) - 1
        print()

        while left2 <= right2:
            mid2 = (left2 + right2) // 2
            # print(mid2)
            if nums[mid2] == target:
                # print(mid2)
                return mid2
            elif nums[mid2] > target:
                right2 = mid2 -1
                print("right2: " + str(right2))
            else:
                left2 = mid2 + 1
                print("left2: " + str(left2))
            
        return -1
        