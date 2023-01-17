class Solution:
    def fib(self, n: int) -> int:
        def helper(n):  
            if(n<2):
                return n
            return helper(n-1) + helper(n-2)
        return helper(n)