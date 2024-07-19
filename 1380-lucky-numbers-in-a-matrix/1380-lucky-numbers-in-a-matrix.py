class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        rowMins = [min(row) for row in matrix]
        colMaxs = [
            max([
                matrix[r][c] for r in range(m)
            ]) for c in range(n)
        ]
        
        return [n for n in rowMins if n in colMaxs]