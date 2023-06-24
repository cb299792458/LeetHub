class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        memo = {}
        
        def dfs(diff,i):
            if (diff,i) in memo: return memo[(diff,i)]
            
            if i==len(rods):
                if diff: return -float('inf')
                else: return 0
                
            r=rods[i]
            i+=1
            
            res = max(dfs(diff+r,i)+r,dfs(diff-r,i),dfs(diff,i))
            memo[(diff,i-1)]=res
            return res
    
        return dfs(0,0)