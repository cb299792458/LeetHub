class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = ((0,1), (1,0), (0,-1), (-1,0))
        di = 0
        r,c = 0,0
        R,C = len(matrix),len(matrix[0])
        
        elements = [matrix[0][0]]
        seen = set([(0,0)])
        while len(elements)<R*C:
            (dr,dc) = dirs[di%4]
            r+=dr
            c+=dc
            if r<0 or c<0 or r==R or c==C or (r,c) in seen:
                r-=dr
                c-=dc
                di+=1
            else:
                seen.add((r,c))
                elements.append(matrix[r][c])
        return elements