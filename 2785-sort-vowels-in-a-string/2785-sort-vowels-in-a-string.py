class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set([c for c in 'aeiouAEIOU'])
        s_vowels = []
        
        replaced = []
        for c in s:
            if c in vowels:
                replaced.append('')
                s_vowels.append(c)
            else:
                replaced.append(c)
                
        s_vowels.sort()
        s_vowels = deque(s_vowels)
        
        return ''.join([c if c else s_vowels.popleft() for c in replaced])