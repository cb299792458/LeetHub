class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = dict()
        longest = -1
        for i,c in enumerate(s):
            if c in first:
                longest = max(longest, i - first[c] - 1)
            else:
                first[c] = i
        return longest