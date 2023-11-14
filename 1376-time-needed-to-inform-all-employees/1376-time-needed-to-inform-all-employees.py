class Solution:
    def numOfMinutes(self, n: int, headID: int, managers: List[int], informTime: List[int]) -> int:
        subordinates = defaultdict(list)
        
        for employee, manager in enumerate(managers):
            if manager==-1: continue
            subordinates[manager].append(employee)
        # print(subordinates)
        longest = 0
        
        def dfs(emp, time):
            # print(emp, time)
            if not subordinates[emp]:
                nonlocal longest
                longest = max(longest, time)
                return
            
            for sub in subordinates[emp]:
                dfs(sub, time + informTime[emp])
            
        dfs(headID, 0)
        return longest