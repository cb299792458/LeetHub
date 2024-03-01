class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = list(s)
        s.sort(reverse=True)
        s.append(s[0])
        return ''.join(s[1:])