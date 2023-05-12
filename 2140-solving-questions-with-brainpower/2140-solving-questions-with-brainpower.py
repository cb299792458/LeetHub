class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # memo={}
        @cache
        def dp(i):
            if i>=len(questions): return 0
            # if i in memo: return memo[i]
            
            solve = questions[i][0] + dp(i+questions[i][1]+1)
            
            skip = dp(i+1)
            
            # memo[i]=max(solve,skip)
            # return memo[i]
            return max(solve,skip)
        
        return dp(0)