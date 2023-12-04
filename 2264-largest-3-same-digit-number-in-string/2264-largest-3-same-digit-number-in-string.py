class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best = ''
        for i,c in enumerate(num[:-2]):
            if c==num[i+1] and c==num[i+2] and (not best or c>best[0]):
                best = c*3
        return best
            