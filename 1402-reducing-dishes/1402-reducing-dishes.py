class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        best = 0
        curr = 0
        prev = 0
        
        for food in satisfaction:
            curr += prev
            curr += food
            prev += food
            
            best = max(best, curr)
        
        return best