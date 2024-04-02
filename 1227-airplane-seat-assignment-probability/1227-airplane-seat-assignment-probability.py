class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        @cache
        def recur(n):
            if n==1:
                return 1
            if n==2:
                return 1/2
            return recur(n-1)
        
        return recur(n)