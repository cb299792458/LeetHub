class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def dist(orig,dest):
            x1,y1 = orig
            x2,y2 = dest
            return max(abs(y2-y1),abs(x2-x1))
        
        time = 0
        for i in range(len(points)-1):
            time += dist(points[i], points[i+1])
        return time