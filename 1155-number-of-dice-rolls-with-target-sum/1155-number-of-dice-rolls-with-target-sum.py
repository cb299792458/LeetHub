class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        ways = defaultdict(int)
        for i in range(1,k+1):
            ways[i] = 1
        
        for _ in range(n-1):
            new_ways = defaultdict(int)
            for val in range(1,k+1):
                for prev, count in ways.items():
                    new_ways[prev+val] += count
            ways = new_ways
            
        return ways[target] % (10**9+7)