class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for point in points:
            [x, y] = point
            dist = math.sqrt(x**2 + y**2)
            
            heapq.heappush(heap, (dist, point))
        
        res = []
        for _ in range(k):
            closest = heapq.heappop(heap)
            res.append(closest[1])
            
        return res