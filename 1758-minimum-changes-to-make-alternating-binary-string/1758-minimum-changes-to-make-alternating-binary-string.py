class Solution:
    def minOperations(self, s: str) -> int:
        ops = 0
        good = '0'
        for c in s:
            if c!=good:
                ops += 1
            good = '1' if good=='0' else '0'
        return min(ops, len(s)-ops)