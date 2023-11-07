class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        times = [d/s for d,s in zip(dist,speed)]
        times.sort()
               
        for i,time in enumerate(times):
            if time <= i:
                return i
            
        return len(times)