class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 = '#' + text1
        text2 = '*' + text2
        m,n = len(text1), len(text2)
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(1,m):
            for j in range(1,n):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        print(dp)
        return dp[-1][-1]
                                                    