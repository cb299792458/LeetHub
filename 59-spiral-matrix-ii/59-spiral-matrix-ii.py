class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[None for _ in range(n)] for _ in range(n)]
        
        pos=[0,0]
        dirs = [
            [0,1],
            [1,0],
            [0,-1],
            [-1,0]
        ]
        di=0
        
        for i in range(1,n**2+1):
            grid[pos[0]][pos[1]]=i
            
            pos[0]+=dirs[di][0]
            pos[1]+=dirs[di][1]
            
            if pos[0]<0 or pos[1]<0 or pos[0]==n or pos[1]==n or grid[pos[0]][pos[1]]:
                
                pos[0]-=dirs[di][0]
                pos[1]-=dirs[di][1]
                di+=1
                if di==4: di=0
            
                pos[0]+=dirs[di][0]
                pos[1]+=dirs[di][1]
            
        return grid