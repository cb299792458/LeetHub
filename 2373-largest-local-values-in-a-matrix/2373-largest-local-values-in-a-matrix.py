class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)
        res = []
        
        for i in range(1,N-1):
            sub = []
            for j in range(1,N-1):
                val = 1
                for di in [-1,0,1]:
                    for dj in [-1,0,1]:
                        val = max(val, grid[i+di][j+dj])
                sub.append(val)
            res.append(sub)
        
        return res