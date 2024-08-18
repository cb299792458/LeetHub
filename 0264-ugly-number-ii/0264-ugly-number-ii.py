class Solution:
    def nthUglyNumber(self, n: int) -> int:
        seen = set([1])
        ugly = [1]
        factors = (2,3,5)
        current = 1
        
        for _ in range(n):
            current = heapq.heappop(ugly)
            for f in factors:
                new = current * f
                if new not in seen:
                    seen.add(new)
                    heapq.heappush(ugly, new)
        
        return current