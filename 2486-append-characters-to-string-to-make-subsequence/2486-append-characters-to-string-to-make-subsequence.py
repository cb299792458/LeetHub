class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        N = len(t)
        for c in s:
            if i==N:
                break
            if c==t[i]:
                i+=1
        return N-i