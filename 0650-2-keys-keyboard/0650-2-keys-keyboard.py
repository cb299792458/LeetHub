class Solution:
    def minSteps(self, n: int) -> int:
        
        @cache
        def explore(curr, clip):
            if curr == n:
                return 0
            if curr > n:
                return math.inf
            
            copy = 2 + explore(2*curr, curr)
            paste = 1 + explore(curr+clip, clip) if clip else math.inf # clipboard cannnot be empty
            
            return min(copy,paste)
        
        return explore(1,0)
        