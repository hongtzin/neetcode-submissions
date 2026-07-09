class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        startpointer = 0
        endpointer = len(numbers) - 1

        while startpointer < endpointer:
            sum = numbers[startpointer] + numbers[endpointer]
            if sum == target:
                return [startpointer + 1, endpointer + 1]
            if sum < target:
                startpointer +=1
            else:
                endpointer -=1
