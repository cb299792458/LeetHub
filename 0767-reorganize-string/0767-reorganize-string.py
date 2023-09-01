class Solution:
    def reorganizeString(self, s: str) -> str:
        ctr = Counter(s)
        heap = [(-count,char) for [char,count] in ctr.items()]
        heapq.heapify(heap)
        
        # first = heapq.heappop(heap)
        # res = [first[1]]
        # if first[0]+1: heapq.heappush(heap,(first[0]+1,first[1]))
        res = []
        
        
        while heap:
            (count1,char1) = heapq.heappop(heap)
            if not res or res[-1] != char1:
                res.append(char1)
                if count1+1: heapq.heappush(heap,(count1+1,char1))
            else:
                if not heap: return ''
                
                (count2,char2) = heapq.heappop(heap)
                heapq.heappush(heap,(count1,char1))
                res.append(char2)
                if count2+1: heapq.heappush(heap,(count2+1,char2))
        
        return ''.join(res)