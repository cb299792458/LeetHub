class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = []
        for i in range(query_row+2):
            glasses.append([0]*(i+1))
        glasses[0][0]=poured

        for r in range(query_row+1):
            for c in range(len(glasses[r])):
                if glasses[r][c]>1:
                    excess = glasses[r][c]-1
                    glasses[r][c]=1
                    glasses[r+1][c]+=excess/2
                    glasses[r+1][c+1]+=excess/2
        return glasses[query_row][query_glass]
