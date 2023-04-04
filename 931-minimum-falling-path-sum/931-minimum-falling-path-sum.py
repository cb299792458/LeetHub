class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        for r in range(1,n):
            for c in range(n):
                ul = matrix[r-1][c-1] if c>0 else float('inf')
                um = matrix[r-1][c] 
                ur = matrix[r-1][c+1] if c<n-1 else float('inf')
                
                matrix[r][c]+=min(ul,um,ur)
        
        # print(matrix)
        return min(matrix[-1])