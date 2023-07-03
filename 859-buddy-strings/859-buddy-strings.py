class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        diffs=[]
        
        if len(s)!=len(goal): return False
        
        for c1,c2 in zip(s,goal):
            if c1!=c2: diffs.append([c1,c2])
                
        if len(diffs)==0: return len(set(s))!=len(s)
        if len(diffs)!=2: return False
        
        return diffs[1][0]==diffs[0][1] and diffs[1][1]==diffs[0][0]