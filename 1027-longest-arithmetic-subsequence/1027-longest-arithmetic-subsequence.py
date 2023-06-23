class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        def one():
            return 1
        dp = defaultdict(one)
        
        for r in range(len(nums)):
            for l in range(0,r):
                diff = nums[r]-nums[l]
                dp[r,diff] = dp[l,diff] + 1
                
        return max(dp.values())