class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        N = len(times)
        empty_chairs = [i for i in range(N)]
        heapq.heapify(empty_chairs)
        taken_chairs = dict()
        
        events = []
        for i,[a,l] in enumerate(times):
            events.append((a, 'bA', i))
            events.append((l, 'aL', i))
        events.sort()
        
        for (time, event, friend) in events:
            if friend == targetFriend:
                return empty_chairs[0]
            
            if event == 'bA':
                taken_chairs[friend] = heapq.heappop(empty_chairs)
            elif event == 'aL':
                heapq.heappush(empty_chairs, taken_chairs[friend])
        