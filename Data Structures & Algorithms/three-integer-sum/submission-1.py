class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for outerindex in range(len(nums)):
            numtarget = 0 - nums[outerindex]
            # print(numtarget)
            num1set = set()
            hs = set()
            for innerindex in range(len(nums)):
                
                if innerindex == outerindex:
                    continue

                if numtarget - nums[innerindex] in hs:
                    num1set.add(tuple(sorted([numtarget - nums[innerindex], nums[innerindex] ,nums[outerindex]])))
                    # print(sorted([numtarget - nums[innerindex], nums[innerindex] ,nums[outerindex]]))
                    continue
                
                hs.add(nums[innerindex])
                # print(hs)
            # print()
            res.update(num1set)
        final = []
        for element in res:
            final.append(list(element))
        return final