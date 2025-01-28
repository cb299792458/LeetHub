class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        seen = set()

        def dfs(r,c):
            if r<0 or c<0 or r==M or c==N:
                return 0
            if grid[r][c] == 0:
                return 0
            if (r,c) in seen:
                return 0
            seen.add((r,c))

            fish = grid[r][c]
            for d in dirs:
                [dr, dc] = d
                [nr, nc] = [r+dr, c+dc]
                fish += dfs(nr, nc)
            return fish
        
        res = 0
        for r in range(M):
            for c in range(N):
                res = max(res, dfs(r,c))
        return res
        