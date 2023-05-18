class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes = set([i for i in range(n)])
        
        for [_,end] in edges:
            nodes.discard(end)
            
        return nodes