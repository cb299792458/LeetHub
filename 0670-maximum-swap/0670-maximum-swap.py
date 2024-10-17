class Solution:
    def maximumSwap(self, v: int) -> int:
        return int(max([s:=str(v)]+[s[:i]+s[j]+s[i+1:j]+c+s[j+1:] for i,c in enumerate(s) for j in range(i+1,len(s))]))
        
        