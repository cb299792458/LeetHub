class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        perms = []
        def backtrack(prevs):
            if len(prevs)==len(s):
                perms.append(prevs)
                return
            
            idx = len(prevs)
            if s[idx].isnumeric():
                backtrack(prevs+s[idx])
            else:
                backtrack(prevs+s[idx].upper())
                backtrack(prevs+s[idx].lower())
        
        backtrack('')
        return perms