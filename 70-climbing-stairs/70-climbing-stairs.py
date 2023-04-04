class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+2)
        dp[0]=1
        for i in range(len(dp)-2):
            dp[i+1]+=dp[i]
            dp[i+2]+=dp[i]
            
        return dp[n]
        