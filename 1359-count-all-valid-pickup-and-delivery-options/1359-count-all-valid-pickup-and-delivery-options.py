class Solution:
    def countOrders(self, n: int) -> int:
        options=[0,1]
        for i in range(2,n+1):
            options.append(options[-1]*i*(2*i-1))
        return options[-1] % (10**9+7)