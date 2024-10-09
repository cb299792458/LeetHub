class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = adds = 0
        for c in s:
            if c=='(':
                open+=1
            else:
                if open:
                    open-=1
                else:
                    adds+=1
        
        return open + adds