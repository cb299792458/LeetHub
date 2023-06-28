class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj_list=defaultdict(list)
        for ([orig,dest],prob) in zip(edges,succProb):
            adj_list[orig].append((dest,prob))
            adj_list[dest].append((orig,prob))
                
        probs=[0]*n
        heapq=[(-1,start)]
        
        while heapq:
            # print(heapq)
            (prob,node) = heappop(heapq)
            # since python only has minheap, switch to negative!!!
            prob=-prob
            
            # already hit node, not better
            if probs[node]>=prob: continue
            
            # set prob for this node
            probs[node]=prob
            
            # stop at end
            if node==end: return prob
            
            # visit neighbors
            for (neighbor,new_prob) in adj_list[node]:
                heappush(heapq,(-new_prob*prob,neighbor))
                       
        return 0