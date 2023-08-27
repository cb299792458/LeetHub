class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # dp = {}
        # for stone in stones:
        #     dp[stone]=set()
        dp = {stone:set() for stone in stones}
        dp[0].add(1)
        
        for curr in stones[1:]:
            for prev in stones:
                if prev==curr: break
                if curr-prev in dp[prev]:
                    dp[curr].add(curr-prev)
                    dp[curr].add(curr-prev+1)
                    dp[curr].add(curr-prev-1)
        return len(dp[list(dp.keys())[-1]])!=0
                    