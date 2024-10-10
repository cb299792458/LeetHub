class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        monostack = []
        for i, n in enumerate(nums):
            if not monostack or n<monostack[-1][1]:
                monostack.append((i,n))
        
        best = 0
        
        for j in range(len(nums)-1,-1,-1):
            n = nums[j]
            while monostack and monostack[-1][1]<=n:
                best = max(best, j-monostack[-1][0])
                monostack.pop()
        return best