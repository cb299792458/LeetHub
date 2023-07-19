class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end=-float('inf')
        erasures=0
        intervals.sort(key=lambda x: x[1])

        for s,e in intervals:
            if s>=end:
                end=e
            else:
                erasures+=1
        
        return erasures