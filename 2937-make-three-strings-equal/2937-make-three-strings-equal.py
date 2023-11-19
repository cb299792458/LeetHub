class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        [n1,n2,n3] = [len(s) for s in [s1,s2,s3]]
        
        common = 0
        
        while common<min(n1,n2,n3) and s1[common]==s2[common] and s1[common]==s3[common]:
            common+=1
            
        if not common: return -1
        return n1 + n2 + n3 - 3*common