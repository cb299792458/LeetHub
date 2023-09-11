class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        points = 0
        prev_end = -float('inf')
        
        for start,end in nums:
            increase = end + 1 - max(start,prev_end)
            points += increase if increase > 0 else 0
            
            prev_end = max(prev_end,end+1)
            
        return points