class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        self.largest = 0
        def check(n):
            if n<2: return
            for i in range(2,1+int(sqrt(n))):
                if n%i==0: return
            self.largest = max(self.largest, n)
        
        N = len(nums)
        for i in range(N):
            check(nums[i][i])
            check(nums[i][-1-i])
        return self.largest