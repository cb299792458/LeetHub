class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = []
        n=len(grid)
        
        for c in range(n):
            col=[]
            for r in range(n):
                col.append(str(grid[r][c]))
            cols.append("-".join(col))
        
        ans=0
        
        for row in grid:
            for col in cols:
                if "-".join([str(r) for r in row]) == col: ans+=1
        
        return ans