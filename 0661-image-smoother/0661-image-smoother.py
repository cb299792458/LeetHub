class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        R, C = len(img), len(img[0])
        # img = [[img[r][c]/4 for c in range(C)] for r in range(R)]
        
        def smooth(r,c):
            total = 0
            count = 0
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    nr,nc = r+dr,c+dc
                    if -1<nr<R and -1<nc<C:
                        total += img[nr][nc]
                        count+=1
            return total//count
        
        
        return [[smooth(r,c) for c in range(C)] for r in range(R)]
