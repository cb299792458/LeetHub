class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        R,C = len(grid), len(grid[0])
        row_ones,col_ones,row_zeroes,col_zeroes = defaultdict(int),defaultdict(int),defaultdict(int),defaultdict(int)
        
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    row_ones[r]+=1
                    col_ones[c]+=1
                else:
                    row_zeroes[r]+=1
                    col_zeroes[c]+=1
        
        return [[row_ones[r]+col_ones[c]-row_zeroes[r]-col_zeroes[c] for c in range(C)] for r in range(R)]