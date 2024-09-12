class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = bin(start ^ goal)
        return len([c for c in xor if c=='1'])