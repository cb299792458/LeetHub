class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        coords = [[rStart,cStart]]
        dirs = ((0,1), (1,0), (0,-1), (-1,0))
        r, c = rStart, cStart
        step = 0
        
        while len(coords)<rows*cols:
            (dr,dc) = dirs[step%4]
            dist = 1 + step//2
            for _ in range(dist):
                r += dr
                c += dc
                if -1<r<rows and -1<c<cols:
                    coords.append([r,c])
            step+=1
        
        return coords