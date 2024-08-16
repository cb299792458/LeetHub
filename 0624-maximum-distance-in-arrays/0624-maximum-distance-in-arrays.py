class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        small = arrays[0][0]
        large = arrays[0][-1]
        max_dist = 0
        
        for array in arrays[1:]:
            max_dist = max(max_dist, large-array[0], array[-1]-small)
            small = min(small, array[0])
            large = max(large, array[-1])
        
        return max_dist