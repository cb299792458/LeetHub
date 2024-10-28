class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_set = set(nums)
        best = -1
        
        for num in nums:
            curr = 1
            square = num
            while square ** 2 in num_set:
                square *= square
                curr += 1
            if curr>1 and curr>best:
                best = curr
                
        return best