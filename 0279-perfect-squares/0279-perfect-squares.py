class Solution:
    def numSquares(self, n: int) -> int:
        best = n
        squares = [i*i for i in range(1,int(sqrt(n)+1))]
        
        @cache
        def dp(total, nums):
            if total==n:
                nonlocal best
                best = min(nums, best)
                return
            if total>n:
                return
            if nums==4:
                return
            
            for num in squares:
                dp(total+num, nums+1)
        
        dp(0,0)
        return best