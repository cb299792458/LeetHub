class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj_list = []
        for i in range(len(bombs)):
            adjs = []
            [x1,y1,r1] = bombs[i]
            
            for j in range(len(bombs)):
                if i==j: continue
                [x2,y2,_]=bombs[j]
                
                if (x1-x2)**2 + (y1-y2)**2 <= r1**2: adjs.append(j)
            
            adj_list.append(adjs)
        
        def dfs(i,exploded):
            exploded.add(i)
            
            for adj in adj_list[i]:
                if adj not in exploded: dfs(adj,exploded)
            
            return len(exploded)
        
        return max([dfs(i,set()) for i in range(len(bombs))])