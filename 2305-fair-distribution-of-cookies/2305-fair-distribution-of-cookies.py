class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        ans = float('inf')
        distributions=[0]*k
        avg = sum(cookies)//k
        
        def backtrack(cookie,distributions):
            if cookie==len(cookies):
                nonlocal ans
                ans = min(ans,max(distributions))
                return
            
            for child in range(k):
                if distributions[child]>avg: continue
                distributions[child]+=cookies[cookie]
                backtrack(cookie+1,distributions)
                distributions[child]-=cookies[cookie]
                if not distributions[child]: break
        
        backtrack(0,distributions)
        return ans
                