class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        def fill(r,c):
            if r<0 or c<0 or r==M or c==N:
                return
            if grid[r][c] == '0':
                return
            grid[r][c] = '0'
            fill(r-1,c)
            fill(r,c+1)
            fill(r+1,c)
            fill(r,c-1)
        
        islands = 0
        for r in range(M):
            for c in range(N):
                if grid[r][c]=='1':
                    islands += 1
                    fill(r,c)
        return islands