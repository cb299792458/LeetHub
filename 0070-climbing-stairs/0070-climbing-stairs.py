class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0,1,2]
        while len(memo)<=n:
            memo.append(memo[-1]+memo[-2])
        return memo[n]