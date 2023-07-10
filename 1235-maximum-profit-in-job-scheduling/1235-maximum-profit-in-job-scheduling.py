class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profits: List[int]) -> int:
        max_profit=0
        heap=[]
        
        tuples = [(startTime[i],endTime[i],profits[i]) for i in range(len(startTime))]
        tuples.sort()
        
        for (start,end,profit) in tuples:
            while heap and heap[0][0] <= start:
                max_profit = max(max_profit, heappop(heap)[1])
                
            heappush(heap,(end,max_profit+profit))
            
        
        return max(tup[1] for tup in heap)