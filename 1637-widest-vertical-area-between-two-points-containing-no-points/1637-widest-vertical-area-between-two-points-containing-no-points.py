class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = list(set([point[0] for point in points]))
        xs.sort()
        
        best = 0
        for i,x in enumerate(xs[:-1]):
            best = max(best,xs[i+1]-x)
        return best