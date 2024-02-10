class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        pals = 0
        
        for i in range(N):
            # odd
            j=k=i
            while j>-1 and k<N and s[j]==s[k]:
                pals += 1
                j -= 1
                k += 1
                
            # even
            j=i
            k=i+1
            while j>-1 and k<N and s[j]==s[k]:
                pals += 1
                j -= 1
                k += 1
        
        return pals