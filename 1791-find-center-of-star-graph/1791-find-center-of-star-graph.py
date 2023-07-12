class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        connections = defaultdict(int)
        
        for [a,b] in edges:
            if connections[a]: return a
            if connections[b]: return b
            connections[a]+=1
            connections[b]+=1
            