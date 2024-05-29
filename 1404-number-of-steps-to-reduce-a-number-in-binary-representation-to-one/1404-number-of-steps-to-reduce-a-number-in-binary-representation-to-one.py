class Solution:
    def numSteps(self, s: str) -> int:
        n = int(s,2)
        steps = 0
        
        while n>1:
            if n%2:
                n += 1
            else:
                n //= 2
        
            steps += 1
        
        return steps