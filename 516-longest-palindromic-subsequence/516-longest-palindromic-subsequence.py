class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = dict()
        def dfs(l,r):
            if l==r: return 1
            if l>r: return 0
            if str([l,r]) in memo: return memo[str([l,r])]
            
            
            if s[l]==s[r]:
                memo[str([l,r])]=2+dfs(l+1,r-1)
            else:
                memo[str([l,r])]=max(dfs(l+1,r),dfs(l,r-1))
            return memo[str([l,r])]
            
        return dfs(0,len(s)-1)