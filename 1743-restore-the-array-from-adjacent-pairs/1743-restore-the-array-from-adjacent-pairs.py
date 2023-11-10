class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjs = defaultdict(list)
        start_end = set()
        
        for [a,b] in adjacentPairs:
            for p in [a,b]:
                if p in start_end:
                    start_end.remove(p)
                else:
                    start_end.add(p)
                
            adjs[a].append(b)
            adjs[b].append(a)
            
        [start, end] = list(start_end)
        
        orig = [start]
        seen=set(orig)
        while orig[-1] != end:
            new = adjs[orig[-1]][0] if adjs[orig[-1]][0] not in seen else adjs[orig[-1]][1]
            seen.add(new)
            orig.append(new)
            
        return orig