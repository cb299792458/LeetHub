class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp=defaultdict(lambda: defaultdict(lambda: 1))
        
        for r in range(len(nums)):
            for l in range(r):
                diff = nums[r]-nums[l]
                dp[r][diff] = dp[l][diff] + 1
                
        return max( max(vals.values()) for vals in dp.values() )