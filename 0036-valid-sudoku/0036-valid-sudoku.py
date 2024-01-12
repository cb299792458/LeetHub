class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxs = defaultdict(set)
        
        for r, row in enumerate(board):
            for c, n in enumerate(row):
                if n=='.': continue
                    
                if n in rows[r]: return False
                rows[r].add(n)
                if n in cols[c]: return False
                cols[c].add(n)
                
                b = 3*(r//3) + (c//3)

                if n in boxs[b]: return False
                boxs[b].add(n)
        return True