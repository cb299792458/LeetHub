class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        STONE = '#'
        OBSTA = '*'
        EMPTY = '.'
        M, N = len(box), len(box[0])
        
        for r in range(M):
            for c in range(N-1,-1,-1):
                nc = c+1
                while nc<N and box[r][nc-1] == STONE and box[r][nc] == EMPTY:
                    box[r][nc-1], box[r][nc] = box[r][nc], box[r][nc-1]
                    nc += 1
        
        res = [[0 for _ in range(M)] for _ in range(N)]
        
        for r in range(M):
            for c in range(N):
                res[c][M-r-1] = box[r][c]
        
        return res