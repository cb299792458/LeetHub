class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for [a,b] in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        seen = set()
        must = set()
        
        def dfs(node):
            if node in seen: return False
            seen.add(node)
            
            res = hasApple[node]
            for neighbor in graph[node]:
                if dfs(neighbor): res = True
            
            if res:
                must.add(node)
            return res
        
        dfs(0)
        
        return max((len(must)-1)*2,0)