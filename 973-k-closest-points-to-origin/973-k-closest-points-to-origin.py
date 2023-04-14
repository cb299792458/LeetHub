class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_by_distance = dict()
        
        tuples = []
        for point in points:
            dist = math.sqrt( point[0]**2 + point[1]**2 )
        
            tuples.append((dist,point))
            
        heapq.heapify(tuples)

        res = []
        for i in range(k):
            res.append(heapq.heappop(tuples)[1])
        return res