class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counts = Counter(s)
        for c in t:
            if counts[c]:
                counts[c]-=1
            else:
                return c