class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        heapq.heapify(arr)
        maximum = 0
        
        while arr:
            while arr and arr[0]<maximum+1:
                heapq.heappop(arr)
            if arr:
                heapq.heappop(arr)
                maximum+=1
            
        return maximum