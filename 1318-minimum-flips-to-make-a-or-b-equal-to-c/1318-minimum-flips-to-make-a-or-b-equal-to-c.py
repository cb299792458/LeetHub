class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips=0
        while a or b or c:
            if a%2 and b%2 and not c%2: flips+=2
            elif not c%2 and (a%2 or b%2): flips+=1
            elif not a%2 and not b%2 and c%2: flips+=1
            a=a//2
            b=b//2
            c=c//2
        return flips