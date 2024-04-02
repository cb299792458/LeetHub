class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for _ in range(n)] for _ in range(m)]
        memo[0][0] = 1
        
        def get_memo(r,c):
            if r==-1 or c==-1:
                return 0
            return memo[r][c]
        
        for r in range(m):
            for c in range(n):
                if r==0 and c==0: continue
                memo[r][c] = get_memo(r-1,c) + get_memo(r,c-1)
        
        # print(memo)
        return memo[-1][-1]