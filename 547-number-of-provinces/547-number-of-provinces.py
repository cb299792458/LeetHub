class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen=set()
        res = 0
        n = len(isConnected)
        
        def dfs(city):
            if city in seen: 
                return
            
            seen.add(city)
            
            for other in range(n):
                if other==city or not isConnected[city][other]: continue
                dfs(other)
        
        for i in range(n):
            if i not in seen:
                res+=1
                dfs(i)
                
        return res