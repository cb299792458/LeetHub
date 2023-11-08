class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx = abs(sx-fx)
        dy = abs(sy-fy)
        if dx==0 and dy==0 and t==1: return False
        return max(dx,dy)<=t