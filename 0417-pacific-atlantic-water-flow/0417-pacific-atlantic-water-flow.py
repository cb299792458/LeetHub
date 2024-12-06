class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M, N = len(heights), len(heights[0])
        dirs = [[-1,0],[0,1],[1,0],[0,-1]]
        
        def get_set(queue):
            res = set()
            
            while queue:
                (r,c) = queue.popleft()
                if (r,c) in res:
                    continue
                res.add((r,c))
                
                for d in dirs:
                    nr, nc = r+d[0], c+d[1]
                    if nr<0 or nc<0 or nr==M or nc==N:
                        continue
                    if heights[nr][nc] < heights[r][c]:
                        continue
                    queue.append((nr,nc))
            return res
        
        pq = deque()
        aq = deque()
        for r in range(M):
            pq.append((r,0))
            aq.append((r,N-1))
        for c in range(N):
            pq.append((0,c))
            aq.append((M-1,c))
        
        p_set = get_set(pq)
        a_set = get_set(aq)
        
        return list(p_set.intersection(a_set))