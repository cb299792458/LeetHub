class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows,cols=set(),set()
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if not matrix[r][c]:
                    rows.add(r)
                    cols.add(c)
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in rows or c in cols:
                    matrix[r][c]=0