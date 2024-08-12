class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        seen = [[[False] * 4 for _ in range(N)] for _ in range(N)]
        regions = 0
        (U,R,D,L) = quadrants = ('U','R','D','L')
        
        def fill(r,c,q):
            if r<0 or c<0 or r==N or c==N:
                return
            if seen[r][c][q]:
                return
            seen[r][c][q] = True
            
            match(grid[r][c]):
                case ' ':
                    for nq in range(4):
                        if q != nq:
                            fill(r,c,nq)
                case '/':
                    if q==0:
                        fill(r,c,3)
                    if q==3:
                        fill(r,c,0)
                    if q==2:
                        fill(r,c,1)
                    if q==1:
                        fill(r,c,2)
                case '\\':
                    if q==0:
                        fill(r,c,1)
                    if q==1:
                        fill(r,c,0)
                    if q==2:
                        fill(r,c,3)
                    if q==3:
                        fill(r,c,2)
            match(q):
                case 0:
                    fill(r-1,c,2)
                case 1:
                    fill(r,c+1,3)
                case 2:
                    fill(r+1,c,0)
                case 3:
                    fill(r,c-1,1)
        
        for r in range(N):
            for c in range(N):
                for q in range(4):
                    if not seen[r][c][q]:
                        regions += 1
                        fill(r,c,q)
        return regions
            
                