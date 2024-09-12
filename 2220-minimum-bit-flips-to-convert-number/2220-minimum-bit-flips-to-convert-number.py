class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal
        flips = 0
        while xor:
            flips += xor % 2
            xor //= 2
        return flips