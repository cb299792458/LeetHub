class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return sorted(Counter(word1).values()) == sorted(Counter(word2).values()) and sorted(Counter(word1).keys()) == sorted(Counter(word2).keys())