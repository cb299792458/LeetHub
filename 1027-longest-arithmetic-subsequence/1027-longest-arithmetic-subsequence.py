class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp=defaultdict(lambda: defaultdict(lambda: 1))
        ans=0
        
        for r in range(len(nums)):
            for l in range(0,r):
                diff = nums[r]-nums[l]
                dp[r][diff] = dp[l][diff] + 1
                ans = max(ans,dp[r][diff])
                
        return max([max(sub_dict.values()) for sub_dict in dp.values()])