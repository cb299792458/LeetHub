class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        heapq.heappush(heap, (-a, 'a'))
        heapq.heappush(heap, (-b, 'b'))
        heapq.heappush(heap, (-c, 'c'))
        
        res = []
        while heap:
            (count, char) = heapq.heappop(heap)
            if not count:
                break
            
            if len(res)>1 and res[-1] == res[-2] == char:
                (next_count, next_char) = heapq.heappop(heap)
                if not next_count:
                    break
                res.append(next_char)
                heapq.heappush(heap, (next_count+1, next_char))
            
                heapq.heappush(heap, (count, char))
                
            else:
                res.append(char)
                if count:
                    heapq.heappush(heap, (count+1,char))
        
        return ''.join(res)