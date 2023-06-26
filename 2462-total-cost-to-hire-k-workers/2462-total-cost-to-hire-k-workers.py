class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        pq = []
        l,r=0,len(costs)-1
        
        for _ in range(candidates):
            pq.append([costs[l],'head'])
            l+=1
            if l>=r: break
            pq.append([costs[r],'tail'])
            r-=1
            
        heapify(pq)
        
        res=0
        for _ in range(k):
            [cost,location]=heappop(pq)
            res+=cost
            
            if l<=r:
                if location=='head':
                    heappush(pq,[costs[l],'head'])
                    l+=1
                else:
                    heappush(pq,[costs[r],'tail'])
                    r-=1
        return res
                    
                    