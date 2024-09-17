class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1 = Counter(words1)
        words2 = Counter(words2)
        
        return len([w for w in words1.keys() if words1[w]==1 and words2[w]==1])