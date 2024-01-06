class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profits: List[int]) -> int:
        best = 0
        jobs = [(s,e,p) for [s,e,p] in zip(startTime,endTime,profits)]
        jobs.sort()
        
        heap = []
        for s,e,p in jobs:
            while heap and heap[0][0]<=s:
                best = max(best, heapq.heappop(heap)[1])
                
            heapq.heappush(heap,(e,best+p))
        
        return max(t[1] for t in heap)