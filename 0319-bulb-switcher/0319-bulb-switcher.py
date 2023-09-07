class Solution:
    def bulbSwitch(self, n: int) -> int:
        on=0
        for i in range(1,int(math.sqrt(n))+1):
            on+=1
        return on
        