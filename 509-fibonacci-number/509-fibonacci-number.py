class Solution:
    def fib(self, n: int) -> int:
        # def helper(n):  
        #     if(n<2):
        #         return n
        #     return helper(n-1) + helper(n-2)
        # return helper(n)
        memo = [0,1]
        for i in range(2,n+1):
            memo.append(memo[i-1] + memo[i-2])
            # print(i)
        return memo[n]