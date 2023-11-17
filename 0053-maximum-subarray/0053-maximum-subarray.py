class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        prevs = [0] * (N+1)
        maximum = 1*-10**20
        for i,num in enumerate(nums):
            curr = num+prevs[i]
            maximum = max(maximum, curr)
            prevs[i+1] = max(prevs[i+1], curr)
            
        return maximum