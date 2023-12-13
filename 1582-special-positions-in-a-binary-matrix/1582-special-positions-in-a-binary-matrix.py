class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        R,C = len(mat),len(mat[0])
        
        row1s = [0 for _ in range(R)]
        col1s = [0 for _ in range(C)]
        
        for r in range(R):
            for c in range(C):
                if mat[r][c]==1:
                    print(r,c)
                    row1s[r] += 1
                    col1s[c] += 1
        
        print(row1s)
        print(col1s)
        
        ans = 0
        for r in range(R):
            for c in range(C):
                if row1s[r]*col1s[c]==1 and mat[r][c]==1:
                    ans+=1
        return ans