class Solution:
    def soupServings(self, n: int) -> float:
        if n>10000: return 1
        
        @lru_cache(None)
        def dfs(a,b):
            if a<=0 and b>0:
                return 1.0
            if a<=0 and b<=0:
                return 0.5
            if a>0 and b<=0:
                return 0
            
            prob=0
            servings=[(100,0),(75,25),(50,50),(25,75)]
            for s in servings:
                prob+=dfs(a-s[0],b-s[1])/4
            return prob
            
        return dfs(n,n)