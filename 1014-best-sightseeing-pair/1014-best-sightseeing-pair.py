class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best_pair = 0
        best_spot = -math.inf
        
        for i, val in enumerate(values):
            best_spot -= 1
            best_pair = max(best_pair, val + best_spot)
            best_spot = max(best_spot, val)
        
        return best_pair