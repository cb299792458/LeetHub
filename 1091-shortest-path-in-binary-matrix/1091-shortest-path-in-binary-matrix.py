from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dirs=[
            (-1,-1), (-1,0), (-1,1),
            (0,-1), (0,1),
            (1,-1), (1,0), (1,1)
        ]
        
        if grid[0][0]==1: return -1
        
        seen = set()
        queue = deque([(1,0,0)])
        while queue:
            (time,r,c) = queue.popleft()
            if (r,c) == (len(grid)-1,len(grid)-1): return time
            
            for d in dirs:
                (nr,nc) = (r+d[0],c+d[1])

                if -1<nr<len(grid) and -1<nc<len(grid[0]) and not grid[nr][nc] and (nr,nc) not in seen:
                    seen.add((nr,nc))
                    queue.append((time+1,nr,nc))
        return -1