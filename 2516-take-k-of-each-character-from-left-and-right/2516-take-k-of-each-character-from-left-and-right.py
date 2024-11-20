class Solution:
    def takeCharacters(self, s: str, k: int) -> int:       
        a,b,c, = 'a','b','c'
        counts = Counter(s)
        if counts[a]<k or counts[b]<k or counts[c]<k:
            return -1
        
        extras = Counter()
        res = l = 0
        for [r, char] in enumerate(s):
            extras[char] += 1
            while counts[char] - extras[char] < k:
                print(l)
                extras[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return len(s) - res