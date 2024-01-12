class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def check(r,c,num):
            for i in range(9):
                if board[i][c]==num:
                    return False
                if board[r][i]==num:
                    return False
            sr = 3*(r//3)
            sc = 3*(c//3)
            for br in range(sr,sr+3):
                for bc in range(sc,sc+3):
                    if board[br][bc]==num:
                        return False
            return True
        
        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c]=='.':
                        for n in map(str,range(1,10)):
                            if check(r,c,n):
                                board[r][c] = n
                                if solve(): # try with board[r][c]=n
                                    return True
                                else:
                                    board[r][c]='.' # backtrack if no solution found
                        return False # no solution found with current board
            return True
        return solve()