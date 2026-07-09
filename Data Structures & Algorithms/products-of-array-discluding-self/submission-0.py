class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffixarray = [0]
        suffixstart = 1
        for i in range(1,len(nums)):
            suffixstart *=  nums[i-1]
            suffixarray.append(suffixstart)
        invertednums = []
        for i in range(len(nums)-1,-1,-1):
            invertednums.append(nums[i])
        
        # print(suffixarray)
        # # print()
        # print(invertednums)
    
        #### invert the prefix array because u can just use the same algo above.
        invertedprefixarray = [0]
        prefixstart = 1
        for i in range(1,len(nums)):
            prefixstart *=  invertednums[i-1]
            invertedprefixarray.append(prefixstart)
        # print(invertedprefixarray)
        
        ### invert it back to what it should look like.
        prefixarray = [] 
        for i in range(len(invertedprefixarray)-1,-1,-1):
            prefixarray.append(invertedprefixarray[i])
        # print(prefixarray)      
        
        ### the start and end cannot be product because the product always contain a zero element.
        res = [prefixarray[0]]
        
        for i in range(1,len(nums)-1):
            product = prefixarray[i] * suffixarray[i]
            res.append(product)
        res.append(suffixarray[len(nums)-1])


        print(prefixarray, suffixarray)
        print(res)
        return res