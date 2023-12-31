class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = Counter()
        for word in words:
            for char in word:
                counts[char] += 1
        return all(not num%len(words) for num in counts.values())