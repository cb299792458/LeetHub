class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = [[0 for _ in range(n)] for _ in range(m)]
        for r in range(m):
            memo[r][0] += 1
            memo[r][-1] += 1
        for c in range(n):
            memo[0][c] += 1
            memo[-1][c] += 1
            
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        paths = 0
            
        for _ in range(maxMove):
            new_memo = [[0 for _ in range(n)] for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    old = memo[r][c]
                    for d in dirs:
                        [nr,nc] = [r+d[0], c+d[1]]
                        if -1<nr<m and -1<nc<n:
                            new_memo[nr][nc] += old
            paths += memo[startRow][startColumn]
            memo = new_memo
        
        return paths % (10**9 + 7)