class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r=0
        d=0
        senate = [*senate]
        no_r=False
        no_d=False
        while not no_r and not no_d:
            no_r=no_d=True
            for i in range(len(senate)):
                if senate[i]=='R':
                    no_r=False
                    if d:
                        d-=1
                        senate[i]='X'
                    else: r+=1
                elif senate[i]=='D':
                    no_d=False
                    if r:
                        r-=1
                        senate[i]='X'
                    else: d+=1
            if no_r: return "Dire"
            if no_d: return "Radiant"
                        
                        
