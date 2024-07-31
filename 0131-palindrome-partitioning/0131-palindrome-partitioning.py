class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def backtrack(i, prevs):
            if i == len(s):
                res.append(prevs)
                return
            
            for j in range(i+1, len(s)+1):
                
                if s[i:j] == s[i:j][::-1]:
                    backtrack(j, prevs + [s[i:j]])
        
        backtrack(0,[])
        return res