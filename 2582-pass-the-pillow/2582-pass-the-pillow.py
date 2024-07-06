class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        loop = 2*(n-1)
        if time < n:
            return time + 1
        if time < loop:
            return loop - time + 1
        return self.passThePillow(n, time-loop)