# 00100
# 01010
# 01110
class Solution:
    
    def closedIsland(self, grid: List[List[int]]) -> int:

        def fill(r,c):
            print(f'filling {r} {c}')
            if r<0 or r>=len(grid): return
            if c<0 or c>=len(grid[0]): return
            
            if grid[r][c]==1: return
            grid[r][c]=1
            
            fill(r,c+1)
            fill(r+1,c)
            fill(r,c-1)
            fill(r-1,c)
            
        for row in range(len(grid)):
            fill(row,0)
            fill(row,len(grid[0])-1)
            
        for col in range(len(grid[0])):
            fill(0,col)
            fill(len(grid)-1,col)
            
        print(grid)
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==0:
                    fill(row,col)
                    islands+=1
                    
        return islands