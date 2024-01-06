class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profits: List[int]) -> int:
        best = 0
        jobs = [(s,e,p) for [s,e,p] in zip(startTime,endTime,profits)]
        jobs.sort()
        
        heap = []
        for (s,e,p) in jobs:
            while heap and heap[0][0]<=s: # check all paths that end before new start
                best = max(best, heapq.heappop(heap)[1]) # get best profit up to new job
                
            heapq.heappush(heap,(e,best+p)) # add result of doing new job to heap
        
        return max(t[1] for t in heap)