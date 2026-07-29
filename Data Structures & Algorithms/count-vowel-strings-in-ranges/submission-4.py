class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefixSum = [0] * (len(words) + 1)
        # print(prefixSum)
        total = 0 
        vowels = set(['a','e','i','o','u'])
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                total+=1
            prefixSum[i+1] = total
        ans = [0] * len(queries)
        i = 0 
        for li,ri in queries:
            ans[i] = prefixSum[ri+1] - prefixSum[li]
            i+=1

        return ans