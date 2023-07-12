class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split(' ')
        code = dict()
        seen=set()
        
        if len(pattern)!=len(words): return False
        for char,word in zip(pattern,words):
            if char not in code:
                if word in seen: return False
                code[char]=word
                seen.add(word)
            else:
                if code[char]!=word:return False
        return True