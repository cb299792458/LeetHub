class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        def manhattan(a,b):
            return abs(a[0]-b[0])+abs(a[1]-b[1])
        
        adjs=defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i!=j:
                    adjs[i].append((manhattan(points[i],points[j]),j))
        
        total_cost = 0
        visited = set([0])
        pq = []
        for tup in adjs[0]:
            heapq.heappush(pq,tup)
        
        while pq:
            while pq and pq[0][1] in visited:
                heapq.heappop(pq)
            if not pq: continue
            (cost, point) = heapq.heappop(pq)
            total_cost += cost
            visited.add(point)
            
            for (c,p) in adjs[point]:
                if p not in visited:
                    heapq.heappush(pq,(c,p))
                    
        return total_cost