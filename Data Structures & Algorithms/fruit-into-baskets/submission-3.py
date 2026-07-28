class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0 

        maxFruits = 0 
        hm = {}
        for r in range(len(fruits)):
            if len(hm) == 2:
                
                if fruits[r] not in hm:
                    
                    l = max(hm.values())
                    min_key = min(hm, key = hm.get)
                    del hm[min_key]
                    hm[fruits[r]] = r
                else: #it is in hm
                    maxFruits = max(maxFruits,r-l +1)
                    if fruits[r] != fruits[r-1]:
                        hm[fruits[r]] = r
                    else:
                        pass
            else:
                if fruits[r] not in hm:
                    hm[fruits[r]] = r
                else:
                    if fruits[r] != fruits[r-1]:
                        hm[fruits[r]] = r
                    else:
                        pass
            print(l,r)
            print(hm)
        maxFruits = max(maxFruits, r-l+1)
        return maxFruits
             