class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortednums = sorted(nums)
        res = []
        for outerindex, outernum in enumerate(sortednums):

            if outernum > 0: #the idea is that once it is sorted, any number to the right cannot equal to 0.
                break
            
            if outerindex > 0 and outernum == sortednums[outerindex-1]: # this is to avoid duplicates. outerindex > 0 because outerindex -1 will result in index error.
                continue

            l = outerindex + 1 # needs to be + 1 so that u can get the next index
            r = len(sortednums) - 1
            while l < r:
                if outernum + sortednums[l] + sortednums[r] > 0:
                    r-=1
                
                elif outernum + sortednums[l] + sortednums[r] < 0:
                    l+=1
                else:
                    res.append([outernum,sortednums[l], sortednums[r]])
                    l+=1
                    r-=1
                    while sortednums[l] == sortednums[l-1] and l < r: # same logic as outerindex. 
                        l+=1
                        
        return res