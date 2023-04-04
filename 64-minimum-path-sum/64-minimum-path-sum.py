class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for subarray in grid:
            subarray.append(float('inf'))
        grid.append([float('inf')]*len(grid[0]))
        
        
        for row in range(len(grid)-2,-1,-1):
            for col in range(len(grid[0])-2,-1,-1):
                if row==len(grid)-2 and col==len(grid[0])-2: continue
                grid[row][col]+=min(grid[row][col+1],grid[row+1][col])
                
                
        # print(grid)
        return grid[0][0]