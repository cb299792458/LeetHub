class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = [0] * 366
        for day in range(1,366):
            if day not in days:
                memo[day] = memo[day-1]
                continue
            
            today = memo[day-1] + costs[0]
            seven = memo[day-7] + costs[1]
            thirty = memo[day-30] + costs[2]

            memo[day] = min(today, seven, thirty)
        
        return memo[365]