class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.adjs = defaultdict(dict)
        self.n = n
        for [start,end,cost] in edges:
            self.adjs[start][end] = cost
        

    def addEdge(self, edge: List[int]) -> None:
        [start, end, cost] = edge
        # if end not in self.adjs[start]:
        self.adjs[start][end] = cost
        # else:
        #     self.adjs[start][end] = min(self.adjs[start][end], cost)
        

    def shortestPath(self, node1: int, node2: int) -> int:        
        pq = [(0,node1)]
        visited = set([node1])
        
        while pq:
            cost, node = heapq.heappop(pq)
            if node==node2: return cost
            
            neighbors = list(self.adjs[node].items())
                        
            for [next_node, next_cost] in neighbors:
                if next_node in visited: continue
                heapq.heappush(pq,(cost+next_cost,next_node))
            
            visited.add(node)
        
        return -1
