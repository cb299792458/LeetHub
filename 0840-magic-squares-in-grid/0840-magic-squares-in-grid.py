class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        M,N = len(grid),len(grid[0])
        for r0 in range(M-2):
            for c0 in range(N-2):
                rows = [0,0,0]
                cols = [0,0,0]
                d1,d2 = 0,0
                seen = set()
                for dr in [0,1,2]:
                    for dc in [0,1,2]:
                        r,c = r0+dr, c0+dc
                        num = grid[r][c]
                        if num<1 or num>9:
                            break
                        seen.add(num)
                        rows[dr] += num
                        cols[dc] += num
                        if dr+dc==2:
                            d1+=num
                        if dr-dc==0:
                            d2+=num
                
                if len(seen)==9 and rows[0]==rows[1]==rows[2]==cols[0]==cols[1]==cols[2]==d1==d2:
                    count += 1
        return count