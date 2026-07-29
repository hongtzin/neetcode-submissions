class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        latestfree = 0
        total = 0 
        for arrival, dur in customers:
            if latestfree <= arrival:
                latestfree = arrival + dur
                total += dur
            else:
                total += latestfree + dur - arrival
                latestfree = latestfree + dur

        return total/len(customers)