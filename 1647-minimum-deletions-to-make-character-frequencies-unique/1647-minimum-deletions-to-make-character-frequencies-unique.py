class Solution:
    def minDeletions(self, s: str) -> int:
        counts = Counter(s)
        letters = sorted(counts.keys(), key=lambda k: counts[k], reverse=True)
        
        seen = set()
        deletions = 0
        
        for l in letters:
            while counts[l] and counts[l] in seen:
                counts[l]-=1
                deletions+=1
            seen.add(counts[l])
            
        return deletions
