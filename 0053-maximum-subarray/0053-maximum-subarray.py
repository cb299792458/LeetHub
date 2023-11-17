class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prevs = [0] * (len(nums)+1)
        maximum = -float('inf')
        for i,num in enumerate(nums):
            curr = num+prevs[i]
            maximum = max(maximum, curr)
            prevs[i+1] = max(prevs[i+1], curr)
            
        return maximum