class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        q=defaultdict(float)
        q[(row,column)]=1.0
        
        dirs=(
            (1,2),
            (2,1),
            (-1,2),
            (2,-1),
            (1,-2),
            (-2,1),
            (-1,-2),
            (-2,-1),
        )
        
        moves=0
        while moves<k:
            new_q=defaultdict(float)
            for (r,c) in q:
                prob=q[(r,c)]
                for d in dirs:
                    nr,nc = r+d[0],c+d[1]
                    if nr<0 or nc<0 or nr>=n or nc>=n:
                        continue
                    new_q[(nr,nc)]+=prob/8
            moves+=1
            q=new_q
        # print(q,sum(q.values()))
        return sum(q.values())