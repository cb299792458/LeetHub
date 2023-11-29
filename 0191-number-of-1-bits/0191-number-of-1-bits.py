class Solution:
    def hammingWeight(self, n: int) -> int:
        ones=0
        while n:
            ones += n % 2
            n //= 2
        return ones