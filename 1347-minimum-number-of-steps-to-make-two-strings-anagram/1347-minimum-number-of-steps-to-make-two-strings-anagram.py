class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counts = Counter(s) - Counter(t)
        
        return sum(counts.values())