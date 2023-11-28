class Solution:
    def numberOfWays(self, corridor: str) -> int:
        if corridor.count('S')%2 or corridor.count('S')<2: return 0
        
        plants=0
        seats=0
        ways=1
        
        for c in corridor:
            if c=='S':
                seats+=1
                if seats>2:
                    seats=1
                    ways*=plants+1
                    plants=0
            else:
                if seats==2:
                    plants+=1
        return ways % (10**9+7)
