class Solution:
    def bulbSwitch(self, n: int) -> int:
        on=0
        for i in range(int(math.sqrt(n))):
            on+=1
        return on
        