class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m,n = len(board), len(board[0])
        copy = [row[:] for row in board]
        
        def state(r,c):
            if r<0 or c<0 or r==m or c==n:
                return 0
            return copy[r][c]
        
        def neighbors(r,c):
            res = 0
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    if not dr and not dc:
                        continue
                    if state(r+dr,c+dc):
                        res += 1
            return res
        
        for r in range(m):
            for c in range(n):
                nbrs = neighbors(r,c)
                if copy[r][c]:
                    if nbrs < 2 or nbrs > 3:
                        board[r][c] = 0
                else:
                    if nbrs == 3:
                        board[r][c] = 1
        return board