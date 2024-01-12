class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        count = 0
        for c in s[:len(s)//2]:
            if c in vowels:
                count += 1
        for c in s[len(s)//2:]:
            if c in vowels:
                count -= 1
        
        return count==0