class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        times = [d/s for d,s in zip(dist,speed)]
        times.sort()
        
        eliminated = 0
        
        for i,time in enumerate(times):
            if time <= i:
                break
            
            eliminated+=1
            
        return eliminated