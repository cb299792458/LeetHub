class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counts = Counter(s)
        for c in t:
            counts[c] -= 1
        
        return sum(abs(v) for v in counts.values())//2