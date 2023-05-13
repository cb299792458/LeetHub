from collections import defaultdict
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp=defaultdict(int)
        dp[0]=1
        for i in range(1,high+1):
            if i>=zero:
                dp[i]+=dp[i-zero]
            if i>=one:
                dp[i]+=dp[i-one]
            
        # print(dp)
        sum=0
        for i in range(low,high+1):
            sum+=dp[i]
        return sum % (10**9+7)