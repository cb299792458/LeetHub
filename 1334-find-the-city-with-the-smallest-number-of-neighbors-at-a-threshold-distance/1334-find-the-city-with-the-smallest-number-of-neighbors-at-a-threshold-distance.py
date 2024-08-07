class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        def neighbors(city):
            seen = set()
            q = [(0, city)]
            
            while q:
                (dist, curr) = heapq.heappop(q)
                if curr in seen:
                    continue
                if dist > distanceThreshold:
                    continue
                
                seen.add(curr)
                for [fr, to, wt] in edges:
                    if fr == curr:
                        heapq.heappush(q, (dist+wt, to))
                    if to == curr:
                        heapq.heappush(q, (dist+wt, fr))
            
            return seen
        
        ans = None
        least = float('inf')
        for city in range(n):
            nbrs = len(neighbors(city))
            if nbrs <= least:
                least = nbrs
                ans = city
        
        return ans