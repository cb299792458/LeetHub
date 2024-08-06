class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = list(Counter(word).values())
        counts.sort(reverse=True)
        pushes = 0
        for i, count in enumerate(counts):
            pushes += count*(1 + (i//8))
            
        return pushes