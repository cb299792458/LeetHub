class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        value = sum(i*n for i,n in enumerate(nums))
        total = sum(nums)
        best = value
        
        for n in nums[:0:-1]:
            value += total
            value -= len(nums)*n
            best = max(best, value)
        
        return best