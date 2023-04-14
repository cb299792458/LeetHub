class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones)>1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if y!=x:
                heapq.heappush(stones,y-x)
                
        return 0 if not len(stones) else -stones[0]
