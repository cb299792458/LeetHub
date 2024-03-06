class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount+1)
        dp[0]=0
        
        for i in range(amount+1):
            if dp[i]==-1: continue
            for coin in coins:
                new = i+coin
                if new > amount: continue
                if dp[new] == -1: dp[new] = 1+dp[i]
                else: dp[new] = min(dp[new],1+dp[i])
                    
        return dp[-1]