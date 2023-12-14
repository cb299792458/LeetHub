class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        R,C = len(grid), len(grid[0])
        row_ones,col_ones = defaultdict(int),defaultdict(int)
        
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    row_ones[r]+=1
                    col_ones[c]+=1
        
        return [[2*row_ones[r]+2*col_ones[c]-R-C for c in range(C)] for r in range(R)]