class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        [c1,c2] = map(Counter,[word1,word2])
        return c1.keys()==c2.keys() and sorted(c1.values())==sorted(c2.values())