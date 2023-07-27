class Solution:
    def fillCups(self, amount: List[int]) -> int:
        heap = [-a for a in amount]
        heapq.heapify(heap)
        
        seconds=0
        while heap[0]:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            if a: a+=1
            if b: b+=1
            heapq.heappush(heap,a)
            heapq.heappush(heap,b)
            seconds+=1
            
        return seconds