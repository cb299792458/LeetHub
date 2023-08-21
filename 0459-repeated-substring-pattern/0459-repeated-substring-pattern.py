class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for l in range(1,(len(s)//2)+1):
            if s[:l]*(len(s)//l)==s:
                return True
            
        return False