class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        before = []
        after = []
        start, end = newInterval


        for interval in intervals:
            if interval[1] < start:
                before.append(interval)
            elif interval[0] > end:
                after.append(interval)
            
            
            else:
                start = min(start,interval[0])
                end = max(end,interval[1])

        return before + [[start,end]] + after 