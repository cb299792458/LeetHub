class Solution:
    def numSquares(self, n: int) -> int:
        
        @cache
        def bfs(num):
            if num==0:
                return 0
            if num<0:
                return n
            best = n
            for i in range(1, int(sqrt(n)+1)):
                best = min(best, bfs(num-i*i)+1)
            return best
        
        return bfs(n)