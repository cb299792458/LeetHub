class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        R,C = len(matrix), len(matrix[0])
        transpose = []
        for c in range(C):
            temp = []
            for r in range(R):
                temp.append(matrix[r][c])
            transpose.append(temp)
        return transpose
        
        return list(zip(*matrix))
        
        return [[matrix[r][c] for r in range(R)] for c in range(C)]
