class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjs = defaultdict(list)
        for [s,e] in tickets:
            adjs[s].append(e)
        for l in adjs.values():
            l.sort(reverse=True)
            
        itinerary = []
        def helper(node):
            while adjs[node]:
                helper(adjs[node].pop())
            itinerary.append(node)
        
        helper('JFK')
        return itinerary[::-1]
        