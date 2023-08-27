class Solution:
    def canCross(self, stones: List[int]) -> bool:

        dp = {stone:set() for stone in stones}
        dp[0].add(1)
        
        for curr in stones[1:]:
            for prev in stones:
                k = curr-prev
                if not k: break
                if k in dp[prev]:
                    dp[curr].add(k)
                    dp[curr].add(k+1)
                    dp[curr].add(k-1)
        return dp[stones[-1]]
                    