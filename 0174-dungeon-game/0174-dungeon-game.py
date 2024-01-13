class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        R,C = len(dungeon),len(dungeon[0])

        table = [[10**20 for _ in range(C+1)] for _ in range(R+1)]
        table[R][C-1] = table[R-1][C] = 1
        
        for r in range(R-1,-1,-1):
            for c in range(C-1,-1,-1):
                next = min(table[r+1][c],table[r][c+1])
                table[r][c] = max(next - dungeon[r][c], 1)
                
        return table[0][0]