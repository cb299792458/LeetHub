class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = [[] for _ in range(n)]
        for emp,man in enumerate(manager):
            if man!=-1: subordinates[man].append(emp)
                
        def dfs(id):
            next = 0
            for sub in subordinates[id]:
                next = max(next,dfs(sub))
            return next + informTime[id]
                
        return dfs(headID)