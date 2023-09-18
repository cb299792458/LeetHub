class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        pq = []
        
        for i in range(len(mat)):
            row = mat[i]
            heapq.heappush(pq,(sum(row),i))
            
        res = []
        for _ in range(k):
            res.append(heapq.heappop(pq)[1])
            
        return res