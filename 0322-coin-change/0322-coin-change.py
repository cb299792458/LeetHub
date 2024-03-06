class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def bfs(amount):
            if amount==0:
                return 0
            if amount<0:
                return math.inf
            
            return 1 + min(bfs(amount - coin) for coin in coins)
        
        return bfs(amount) if bfs(amount)<math.inf else -1