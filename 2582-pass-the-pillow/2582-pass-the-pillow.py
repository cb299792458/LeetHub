class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time < n:
            return time + 1
        if time < 2*(n-1):
            return (2*n) - time - 1
        return self.passThePillow(n, time-(2*(n-1)))