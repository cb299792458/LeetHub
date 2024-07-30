class Solution:
    def minimumDeletions(self, s: str) -> int:
        N = len(s)
        dp = [0 for _ in range(N+1)]
        bs = 0
        
        for i, c in enumerate(s):
            if c=='b':
                dp[i+1] = dp[i]
                bs += 1
            else: 
                dp[i+1] = min(dp[i]+1, bs)
        
        return dp[-1]