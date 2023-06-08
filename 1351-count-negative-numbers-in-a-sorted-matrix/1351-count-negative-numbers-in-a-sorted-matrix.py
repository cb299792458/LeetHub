class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        
        res=0
        row,col=0,n-1
        while row<m:            
            if grid[row][col]>=0 or col==-1:
                res += n-col-1
                row+=1
            else:
                col-=1
                
        return res