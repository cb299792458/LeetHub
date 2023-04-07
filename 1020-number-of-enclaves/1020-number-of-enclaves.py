class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
                
        def fill(r,c):
            if r<0 or r>=m: return
            if c<0 or c>=n: return
            
            if grid[r][c]==0: return
            grid[r][c]=0
            
            fill(r,c+1)
            fill(r+1,c)
            fill(r,c-1)
            fill(r-1,c)
        
        for r in range(m):
            fill(r,0)
            fill(r,n-1)
            
        for c in range(n):
            fill(0,c)
            fill(m-1,c)
            
        count=0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1: count+=1
                    
        return count