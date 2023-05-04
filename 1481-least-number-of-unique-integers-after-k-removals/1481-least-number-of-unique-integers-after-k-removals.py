class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = Counter(arr)
        
        freqs = [(f,n) for (n,f) in counts.items()]
        freqs.sort(key=lambda x: x[0], reverse=True)
        print(freqs)
        # freqs=deque(freqs)
        
        while k>0:
            if k>=freqs[-1][0]:
                k-=freqs[-1][0]
                freqs.pop()
            else: break
                
            
            
            
        
        return len(freqs)