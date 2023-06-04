class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen=set()
        res = 0
        
        def dfs(city):
            if city in seen: 
                return
            
            seen.add(city)
            
            for other in range(len(isConnected)):
                if other==city: continue
                if not isConnected[city][other] and not isConnected[other][city]: continue
                dfs(other)
        
        for i in range(len(isConnected)):
            if i not in seen:
                res+=1
                dfs(i)
                
        return res