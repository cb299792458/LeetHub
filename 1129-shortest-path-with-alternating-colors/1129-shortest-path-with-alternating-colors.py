class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        def make_adj_list(edge_list):
            res = defaultdict(list)
            for start, end in edge_list:
                res[start].append(end)
            return res
        answer = [-1 for _ in range(n)]
        red_adj = make_adj_list(redEdges)
        blue_adj = make_adj_list(blueEdges)
        
        visited = set([(0,None)])
        queue = deque([(0,0,None)]) #(node,length,prev_color)
        while queue:
            node,length,color = queue.popleft()
            
            if answer[node]==-1:
                answer[node]=length
            
            if color != 'RED':
                for next_node in red_adj[node]:
                    if (next_node,"RED") not in visited:
                        visited.add((next_node,"RED"))
                        queue.append((next_node,length+1,'RED'))
            if color != 'BLUE':
                for next_node in blue_adj[node]:
                    if (next_node,"BLUE") not in visited:
                        visited.add((next_node,"BLUE"))
                        queue.append((next_node,length+1,'BLUE'))
            

        return answer
