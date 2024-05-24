class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        
        memo = [None] * (N+1)
        memo[N] = True
        
        def dfs(i):
            if memo[i] != None:
                return memo[i]
            
            for word in wordDict:
                j = i + len(word)
                if word == s[i:j]:
                    if dfs(j):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        
        return dfs(0)