class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dirs=((0,1),(0,-1),(1,0),(-1,0))
        
        tuples=[]
        for r in range(m):
            for c in range(n):
                tuples.append((grid[r][c],r,c))
        tuples.sort()
        
        memo=[[1 for _ in range(n)] for _ in range(m)]
        
        for (curr,r,c) in tuples:
            for d in dirs:
                (nr,nc) = (r+d[0],c+d[1])
                if nr<0 or nc<0 or nr==m or nc==n: continue
                prev=grid[nr][nc]
                if curr>prev: memo[r][c]+=memo[nr][nc]
        
        # print(memo)
        return sum([sum(row) for row in memo]) % (10**9+7)