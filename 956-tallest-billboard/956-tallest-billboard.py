class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        @lru_cache(None)
        def dfs(diff,i):
            if i==len(rods):
                if diff: return -float('inf')
                else: return 0
                
            r=rods[i]
            i+=1
            return max(dfs(diff+r,i)+r,dfs(diff-r,i),dfs(diff,i))
    
        return dfs(0,0)