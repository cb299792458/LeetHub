class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts = set()
        ends = []
        
        for [start, end] in paths:
            starts.add(start)
            ends.append(end)
            
        for end in ends:
            if end not in starts:
                return end