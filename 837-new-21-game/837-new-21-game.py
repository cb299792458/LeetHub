class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [None if i < k else 1 if i < n+1 else 0 for i in range(n+maxPts)]
        
        # for i in range(k-1,-1,-1):
        #     dp[i] = (sum(dp[i+1:i+maxPts+1]) / (maxPts))
        
        total = sum(dp[k:])
        for i in range(k-1,-1,-1):
            dp[i] = total / maxPts
            total -= dp[i+maxPts]
            total += dp[i]
            
        print(dp)
        return dp[0] if dp[0]<=1 else 1