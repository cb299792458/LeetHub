class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        
        @cache
        def dfs(r,c):
            if c==N-1:
                return 0
            
            top, mid, bot = 0, 0, 0
            if r>0 and grid[r][c]<grid[r-1][c+1]:
                top = 1 + dfs(r-1,c+1)
            if grid[r][c]<grid[r][c+1]:
                mid += 1 + dfs(r,c+1)
            if r<M-1 and grid[r][c]<grid[r+1][c+1]:
                bot += 1 + dfs(r+1,c+1)
        
            return max(top, mid, bot)
        
        return max(dfs(r,0) for r in range(M))