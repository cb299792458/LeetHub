class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        ans = float('inf')
        distributions=[0]*k
        
        def backtrack(cookie,distributions):
            if cookie==len(cookies):
                nonlocal ans
                ans = min(ans,max(distributions))
                return
            
            for child in range(k):
                distributions[child]+=cookies[cookie]
                backtrack(cookie+1,distributions)
                distributions[child]-=cookies[cookie]
                if not distributions[child]: break
        
        backtrack(0,distributions)
        return ans
                