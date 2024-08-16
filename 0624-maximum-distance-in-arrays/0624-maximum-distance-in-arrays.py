class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        small = math.inf
        large = -math.inf
        max_dist = 0
        
        for array in arrays:
            curr_small, curr_large = array[0], array[-1]
            max_dist = max(max_dist, large-curr_small, curr_large-small)
            small = min(small, curr_small)
            large = max(large, curr_large)
        
        return max_dist