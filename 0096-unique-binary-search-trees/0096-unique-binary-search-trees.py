class Solution:
    def numTrees(self, n: int) -> int:
        dp=[1,1]
        for i in range(2,n+1): # total nodes
            count=0
            for j in range(i):
                count+=dp[j]*dp[i-j-1] # nodes on left * nodes on right
            dp.append(count)
                
        return dp[n]