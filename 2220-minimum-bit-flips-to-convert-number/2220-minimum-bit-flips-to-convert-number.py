class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = bin(start ^ goal)
        return sum(1 if c=='1' else 0 for c in xor)