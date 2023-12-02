class Solution:
    def romanToInt(self, s: str) -> int:
        val = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        num = 0
        
        for i,c in enumerate(s):
            if i<len(s)-1 and val[c]<val[s[i+1]]:
                num -= val[c]
            else:
                num += val[c]
        
        return num