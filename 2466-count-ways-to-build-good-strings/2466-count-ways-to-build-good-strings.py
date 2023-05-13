from collections import defaultdict
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp=defaultdict(int)
        dp[0]=1
        for i in range(1,high+1):
            if i>=zero:
                dp[i] = (dp[i-zero]+dp[i]) % (10**9+7)
            if i>=one:
                dp[i] = (dp[i-one]+dp[i]) % (10**9+7)

        sum=0
        for i in range(low,high+1):
            sum = (sum + dp[i]) % (10**9+7)
        return sum