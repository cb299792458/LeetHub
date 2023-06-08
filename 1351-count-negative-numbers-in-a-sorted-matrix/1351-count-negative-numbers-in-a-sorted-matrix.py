class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        
        res=0
        row,col=0,n-1
        while row<m:
            # print(f'row is {row} and col is {col} and res is {res}')
            
            if grid[row][col]>=0 or col==-1:
                res += n-col-1
                row+=1
            else:
                col-=1
                
        return res