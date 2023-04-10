class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda a: a[0])
        stack = deque([intervals[0]])
        
        for i in range(1,len(intervals)):
            if stack[-1][1]>=intervals[i][0]:
                stack[-1] = [stack[-1][0],max(stack[-1][1],intervals[i][1])]
            else:
                stack.append(intervals[i])
        return [*stack]