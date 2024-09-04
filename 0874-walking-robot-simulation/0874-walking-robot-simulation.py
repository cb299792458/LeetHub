class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        r,c = 0,0
        di = 0
        dirs = [
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        ]
        obstacles = set([(o[1],o[0]) for o in obstacles])
        best = 0
        
        for com in commands:
            if com==-1:
                di+=1
            elif com==-2:
                di-=1
            else:
                (dr,dc) = dirs[di%4]
                for _ in range(com):
                    if (r+dr,c+dc) not in obstacles:
                        r+=dr
                        c+=dc
                best = max(best, (r**2) + (c**2))
        return best