class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = defaultdict(lambda: defaultdict(int))
        N = len(nums)
        count = 0
        
        for i in range(1,N):
            for j in range(i):
                diff = nums[j]-nums[i]
                dp[i][diff] += dp[j][diff] + 1
                count += dp[j][diff]
        
        return count