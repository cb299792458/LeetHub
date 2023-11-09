class Solution:
    def countHomogenous(self, s: str) -> int:
        prev = ''
        streak = 0
        mod = 10**9 + 7
        homogenous = 0
        
        for c in s:
            if c==prev:
                streak += 1
            else:
                streak = 1
                prev = c
                
            homogenous += streak
            
        return homogenous % mod