class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = defaultdict(lambda: defaultdict(int))
        N = len(nums)
        count = 0
        
        for i in range(1,N): # 3rd num
            for j in range(i): # 2nd num
                diff = nums[j]-nums[i]
                
                # i -> j starts a new sequence
                # one more sequence at i than at j
                dp[i][diff] += dp[j][diff] + 1
                
                # if there were sequences ending at j
                # all those sequences have length >=3 at i
                count += dp[j][diff]
        
        return count