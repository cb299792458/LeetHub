class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0: return False
        if n==1: return True
        return not n%2 and self.isPowerOfTwo(n/2)