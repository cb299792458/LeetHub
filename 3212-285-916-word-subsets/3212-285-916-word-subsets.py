class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counts = Counter()
        for word in words2:
            curr = Counter(word)
            for [char, count] in curr.items():
                counts[char] = max(counts[char], count)
        
        def isValid(word):
            curr = Counter(word)
            return all(curr[c] >= counts[c] for c in counts)
        
        return [w for w in words1 if isValid(w)]