class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = 10 ** 20
        alphabet = 'qwertyuiopasdfghjklzxcvbnm'
        costs = defaultdict(lambda: defaultdict(lambda: INF))
        
        for c in alphabet:
            costs[c][c] = 0
        
        for (old, new, price) in zip(original, changed, cost):
            costs[old][new] = min(costs[old][new], price)
            
        for a in alphabet:
            for b in alphabet:
                for c in alphabet:
                    costs[b][c] = min(costs[b][c], costs[b][a] + costs[a][c])
        
        res = sum(costs[s][t] for (s,t) in zip(source,target))
        return res if res < INF else -1