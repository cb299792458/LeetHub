class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        if not [bool for bool in hasApple if bool]: return 0
        
        graph = defaultdict(list)
        for [a,b] in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        seen = set()
        time=-2
        
        def dfs(node):
            if node in seen: return False
            seen.add(node)
            
            res = hasApple[node]
            for neighbor in graph[node]:
                if dfs(neighbor): res = True
            
            if res:
                nonlocal time
                time+=2
            return res
        dfs(0)
        
        return time