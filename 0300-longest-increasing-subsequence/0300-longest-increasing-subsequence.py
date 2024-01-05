class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N
        for i in range(N):
            for j in range(i+1,N):
                if nums[j]>nums[i]:
                    dp[j] = max(dp[j],1+dp[i])
        return max(dp)