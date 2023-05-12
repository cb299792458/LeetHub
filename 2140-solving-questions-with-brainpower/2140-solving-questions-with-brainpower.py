class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo={}
        def dp(i):
            if i>=len(questions): return 0
            if i in memo: return memo[i]
            
            solve = questions[i][0] + dp(i+questions[i][1]+1)
            
            skip = dp(i+1)
            
            memo[i]=max(solve,skip)
            return memo[i]
        
        return dp(0)