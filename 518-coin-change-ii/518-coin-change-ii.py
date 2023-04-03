class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
#         # PURE DP/MEMO
#         memo=[0]*(amount+1)
#         memo[0]=1

#         for coin in coins:
#             for i in range(coin,amount+1):
#                 memo[i] += memo[i-coin]
        
#         return memo[amount]
        
        memo={}
        
        def dfs(amt,idx):
            if amt<0 or idx==len(coins): return 0
            if amt==0: return 1
            
            if (amt,idx) in memo: return memo[(amt,idx)]
            
            memo[(amt,idx)] = dfs(amt-coins[idx],idx) + dfs(amt,idx+1)
            return memo[(amt,idx)]
        
        
        return dfs(amount,0)