class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        INF = 10**20
        N = len(matrix)
        
        memo = [[INF for _ in range(N+1)] for _ in range(N)]
        memo[0] = matrix[0] + [INF]
        
        for r in range(1,N):
            for c in range(N):
                memo[r][c] = matrix[r][c] + min(memo[r-1][c-1],memo[r-1][c],memo[r-1][c+1])
        
        print(memo)
        return min(memo[-1])
        
        