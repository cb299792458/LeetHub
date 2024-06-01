class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for [i,c] in enumerate(s[:-1]):
            score += abs(ord(c) - ord(s[i+1]))
        return score