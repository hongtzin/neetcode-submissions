class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array1 = [0]
        array1prod = 1
        for i in range(len(nums)-1):
            array1prod *= nums[i]
            array1.append(array1prod)
        # return array1
        array2 = [0]
        array2prod = 1
        for i in range(len(nums)-1, 0, -1):
            # print(i)
            array2prod*= nums[i]
            array2.append(array2prod)
        # return array2
        l = 1
        r = len(array2)-2
        res = [array2[-1]]
        # print(res)
        while l < len(array2) - 1 and r > 0:
            print(l,r)
            prod = array2[r] * array1[l]
            res.append(prod) 
            l += 1
            r -= 1
        res.append(array1[-1])
        return res