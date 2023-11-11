class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.adjs = defaultdict(dict)
        self.n = n
        for [start,end,cost] in edges:
            self.adjs[start][end] = cost

    def addEdge(self, edge: List[int]) -> None:
        [start, end, cost] = edge
        self.adjs[start][end] = cost       

    def shortestPath(self, node1: int, node2: int) -> int:        
        pq = [(0,node1)]
        visited = set([node1])
        
        while pq:
            cost, node = heapq.heappop(pq)
            if node==node2: return cost
                        
            for [next_node, next_cost] in self.adjs[node].items():
                if next_node in visited: continue
                heapq.heappush(pq,(cost+next_cost,next_node))
            
            visited.add(node)
        
        return -1
