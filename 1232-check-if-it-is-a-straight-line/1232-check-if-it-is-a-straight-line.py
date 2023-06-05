class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def slope(p1,p2):
            if p1[0]==p2[0]: return float('inf')
            return (p2[1]-p1[1])/(p2[0]-p1[0])
        
        m = slope(coordinates[0],coordinates[1])
        for i in range(2,len(coordinates)):
            if m!=slope(coordinates[0],coordinates[i]): return False
        return True