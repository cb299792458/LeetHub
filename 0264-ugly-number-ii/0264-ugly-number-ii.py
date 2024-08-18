class Solution:
    def nthUglyNumber(self, n: int) -> int:
        seen = set([1])
        ugly = [1]
        factors = (2,3,5)
        current = 1
        
        for _ in range(n):
            current = heapq.heappop(ugly)
            for f in factors:
                new_ugly = current * f
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(ugly, new_ugly)
        
        return current