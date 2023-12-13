class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        R,C = len(mat),len(mat[0])
        
        row1s = [0] * R
        col1s = [0] * C
        
        for r in range(R):
            for c in range(C):
                if mat[r][c]==1:
                    row1s[r] += 1
                    col1s[c] += 1

        ans = 0
        for r in range(R):
            for c in range(C):
                if row1s[r]*col1s[c]==1 and mat[r][c]==1:
                    ans+=1
        return ans