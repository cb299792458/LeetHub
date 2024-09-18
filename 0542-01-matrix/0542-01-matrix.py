class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        q = deque()
        
        res = [[-1] * N for _ in range(M)]
        
        for r in range(M):
            for c in range(N):
                if mat[r][c]==0:
                    res[r][c]=0
                    q.append((r+1,c,1))
                    q.append((r-1,c,1))
                    q.append((r,c+1,1))
                    q.append((r,c-1,1))
        
        while q:
            (r,c,n) = q.popleft()
            if r<0 or r==M or c<0 or c==N:
                continue
            if res[r][c] != -1:
                continue
            
            res[r][c] = n
            q.append((r+1,c,n+1))
            q.append((r-1,c,n+1))
            q.append((r,c+1,n+1))
            q.append((r,c-1,n+1))
        
        return res