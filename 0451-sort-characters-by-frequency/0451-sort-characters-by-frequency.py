class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        return ''.join(sorted(list(s), reverse=True, key=lambda c: (counts[c],c)))