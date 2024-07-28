class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            if n in seen:
                return False
            if n == 1:
                return True
            
            seen.add(n)
            n = sum(int(d)**2 for d in str(n))