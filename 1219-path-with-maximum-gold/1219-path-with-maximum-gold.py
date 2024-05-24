class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        dirs = [
            [0,1],
            [0,-1],
            [1,0],
            [-1,0]
        ]
        res = 0
        
        def backtrack(r,c):
            if r<0 or c<0 or r==M or c==N or grid[r][c]==0:
                return 0
            
            curr = grid[r][c]
            grid[r][c] = 0
            
            best = 0
            for d in dirs:
                best = max(best, backtrack(r+d[0],c+d[1]))
            
            grid[r][c] = curr
            return curr + best
        
        for r in range(M):
            for c in range(N):
                res = max(res,backtrack(r,c))
        
        return res