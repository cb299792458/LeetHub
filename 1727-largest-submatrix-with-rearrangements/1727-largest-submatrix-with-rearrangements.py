class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        area = 0
        
        heights = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                if not r:
                    heights[r][c] = matrix[r][c]
                else:
                    heights[r][c] = matrix[r][c] + heights[r-1][c] if matrix[r][c] else 0
        
        for row in heights:
            row.sort(reverse=True)
            for c,h in enumerate(row):
                area = max(area,(c+1)*h)
        
        return area