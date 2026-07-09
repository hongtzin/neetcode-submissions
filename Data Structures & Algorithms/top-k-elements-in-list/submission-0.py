class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        array = [[] for i in range(len(nums)+1)]

        for num in nums:
            if num not in hm:
                hm[num] = 0 
            hm[num] += 1
        
        print(hm)
        for key,value in hm.items():
            array[value].append(key)
        print(array)
        res = []
        count = 0 

        for i in range(len(nums), -1, -1):
            print(array[i])
            for poo in array[i]:
                res.append(poo)
                count +=1
                if count == k:
                    return res
