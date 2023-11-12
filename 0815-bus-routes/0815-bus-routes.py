class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target: return 0
        
        sets = [set(route) for route in routes]
        adj_list = defaultdict(set)
        
        for i,s1 in enumerate(sets):
            for j,s2 in enumerate(sets):
                if s1&s2:
                    adj_list[i].add(j)
                    adj_list[j].add(i)
                    
        q = deque()
        for i,s in enumerate(sets):
            if source in s:
                q.append((1,i))
                
        seen = set()
                
        while q:
            (buses, i) = q.popleft()
            route = sets[i]
            
            if target in route:
                return buses
            
            if i in seen:
                continue
            seen.add(i)
            
            for j in adj_list[i]:
                q.append((buses+1,j))
                
        return -1