class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        totals = cost[:2]
        for i in range(2,len(cost)):
            totals.append(cost[i]+min(totals[i-1],totals[i-2]))
        return totals[-1]