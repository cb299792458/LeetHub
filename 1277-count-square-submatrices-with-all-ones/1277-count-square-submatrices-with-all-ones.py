class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(N)] for _ in range(M)]
        
        for r in range(M):
            for c in range(N):
                if matrix[r][c]:
                    if r==0 or c==0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1] ,dp[r-1][c-1])
        
        return sum([sum([dp[r][c] for c in range(N)]) for r in range(M)])