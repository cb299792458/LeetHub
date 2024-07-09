class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = 0
        curr = 0
        for [arrival, time] in customers:
            start = max(curr, arrival)
            curr = start + time
            total += curr - arrival
        return total / len(customers)