class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def test(speed):
            time=0.0
            for d in dist:
                time = math.ceil(time)
                time += d/speed
            return time<=hour
        
        l,r=1,10**7
        if not test(r): return -1
        
        while l<r:
            m=l+(r-l)//2
            if test(m):
                r=m
            else:
                l=m+1
        return l