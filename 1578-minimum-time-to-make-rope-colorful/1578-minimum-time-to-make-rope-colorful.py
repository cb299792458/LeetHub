class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        last_color = colors[0]
        last_cost = neededTime[0]
        cost = 0
        for i in range(1,len(colors)):
            if colors[i]==last_color:
                cost += min(neededTime[i], last_cost)
                last_cost = max(neededTime[i], last_cost)
            else:
                last_color = colors[i]
                last_cost = neededTime[i]
        return cost