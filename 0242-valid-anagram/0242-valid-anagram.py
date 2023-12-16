class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s,t = Counter(s), Counter(t)
        
        for k,v in s.items():
            if t[k]!=v:
                return False
            
        return len(s)==len(t)