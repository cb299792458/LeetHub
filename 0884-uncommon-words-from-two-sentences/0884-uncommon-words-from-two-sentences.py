class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = Counter(s1.split(' '))
        words2 = Counter(s2.split(' '))
        return [key for key in words1.keys() if words1[key] == 1 and key not in words2] + [key for key in words2.keys() if words2[key] == 1 and key not in words1]