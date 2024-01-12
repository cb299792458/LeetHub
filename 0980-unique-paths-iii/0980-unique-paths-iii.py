class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])
        distance = 0
        start = None
        end = None
        for r in range(R):
            for c in range(C):
                if grid[r][c]==1:
                    start = (r,c)
                if grid[r][c]==2:
                    end = (r,c)
                if grid[r][c]!=-1:
                    distance += 1
        self.ways = 0
        dirs =[
            [0,1],
            [0,-1],
            [1,0],
            [-1,0]
        ]
        
        def backtrack(r,c,seen):
            if r<0 or r==R or c<0 or c==C:
                return
            if (r,c) in seen:
                return
            if grid[r][c]==-1:
                return
            
            seen.add((r,c))
            if (r,c) == end:
                if len(seen) == distance:
                    self.ways += 1
                return
            
            for dir in dirs:
                nr,nc = r+dir[0], c+dir[1]
                backtrack(nr,nc,seen.copy())
        
        backtrack(*start,set())
        return self.ways