class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = [[None]*(len(s2)+1) for  _ in range(len(s1)+1)]
        
        def helper(i1,i2):
            if i1==len(s1) and i2==len(s2) and i1+i2==len(s3): return True
            
            if memo[i1][i2]!=None: return memo[i1][i2]
            
            if i1<len(s1) and i1+i2<len(s3) and s1[i1]==s3[i1+i2] and helper(i1+1,i2):
                memo[i1][i2] = True
                return True
            if i2<len(s2) and i1+i2<len(s3) and s2[i2]==s3[i1+i2] and helper(i1,i2+1):
                memo[i1][i2] = True
                return True
            memo[i1][i2] = False
            return False
        
        return helper(0,0)