class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def bfs(amount):
            if amount==0:
                return 0
            if amount<0:
                return math.inf
            
            branches = [1 + bfs(amount - coin) for coin in coins]
            return min(branches)
        
        ans = bfs(amount)
        return ans if ans<math.inf else -1