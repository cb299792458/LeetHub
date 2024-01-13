class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counts = Counter()
        for c in s:
            counts[c] += 1
        for c in t:
            counts[c] -= 1
        
        return sum(abs(v) for v in counts.values())//2