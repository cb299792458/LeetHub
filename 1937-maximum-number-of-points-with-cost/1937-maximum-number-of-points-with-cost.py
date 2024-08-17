class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        M,N = len(points),len(points[0])
        dp = [[0]*N]
        
        for row in points:
            l_prev = [0] * N
            r_prev = [0] * N
            n_best = [0] * N
            
            l_prev[0] = dp[-1][0]
            r_prev[-1] = dp[-1][-1]
            for i in range(1,N):
                l_prev[i] = max(l_prev[i-1]-1, dp[-1][i])
                
                r_i = N-1-i
                r_prev[r_i] = max(r_prev[r_i+1]-1, dp[-1][r_i])
                
            for i in range(N):
                n_best[i] = row[i] + max(l_prev[i], r_prev[i])
            
            dp.append(n_best)
                
        return max(dp[-1])