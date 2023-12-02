class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        pairs=0
        extra=0
        
        for count in counts.values():
            pairs += count // 2
            extra += count % 2
            
        print(pairs, extra)
        return 2 * pairs + (1 if extra else 0)