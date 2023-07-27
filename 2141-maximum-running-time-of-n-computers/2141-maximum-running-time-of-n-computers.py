class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        def check(time):
            extra = sum([min(bat,time) for bat in batteries])

            return extra//n>=time
        
        l,r = 1,sum(batteries)//n
        while l<r:
            m=r-(r-l)//2
            if check(m):
                l=m
            else:
                r=m-1
        return l