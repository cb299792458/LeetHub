class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # nums = [-n for n in nums]
        self.heap = nums
        heapq.heapify(self.heap) # min value queue
        
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]
        
        
#         popped=[]
        
#         for i in range(self.k):
#             popped.append( heapq.heappop(self.heap) )
        
#         res = -popped[-1]
        
#         for ele in popped:
#             heapq.heappush(self.heap,ele)
            
#         return res


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)