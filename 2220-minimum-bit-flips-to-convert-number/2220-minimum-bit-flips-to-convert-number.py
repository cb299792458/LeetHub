class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = bin(start ^ goal)
        return sum(int(c=='1') for c in xor)