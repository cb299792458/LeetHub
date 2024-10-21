class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(si, seen):            
            res = 0
            
            for ei in range(si+1, len(s)+1):
                sub = s[si:ei]
                if sub not in seen:
                    seen.add(sub)
                    res = max(res, 1+backtrack(ei,seen))
                    seen.remove(sub)
            
            return res
        
        return backtrack(0, set())