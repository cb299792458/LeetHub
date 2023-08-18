class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        al = defaultdict(list)
        for [a,b] in roads:
            al[a].append(b)
            al[b].append(a)
        
        mnr=0
        for c in al.keys():
            for d in al.keys():
                if c==d: continue
                mnr = max(mnr, len(al[c])+len(al[d]) - (1 if c in al[d] else 0))
                
        return mnr