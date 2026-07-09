import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        maxpile = max(piles)
        
        l = 1
        r = maxpile
        mink = 1000000001
        while l <= r:
            mid = (l + r)//2
            totalhours = 0    
            for num in piles:
                totalhours += math.ceil(num/mid)
            print(totalhours)
            print(l,r)
            if totalhours > h:
                l = mid + 1
                
            else:
                mink = min(mink,mid)
                r = mid - 1
            print(l,r)
            print()
        return mink
