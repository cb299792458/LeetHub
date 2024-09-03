class Solution:
    def getLucky(self, s: str, k: int) -> int:
        vals = {chr(i+97): str(i+1) for i in range(26)}
        
        num = ''.join(vals[c] for c in s)
        for _ in range(k):
            num = sum(int(c) for c in str(num))
        return num