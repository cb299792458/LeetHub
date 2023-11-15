class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        
        memo = [defaultdict(int) for _ in range(N+1)]
        # memo[nums_passed][current_total] = ways
        memo[0][0] = 1
        
        
        for i in range(N):
            num = nums[i]
            last_col_memo = memo[i]
            for [current_total, ways] in last_col_memo.items():
            
                memo[i+1][current_total+num] += ways
                memo[i+1][current_total-num] += ways
        
        return memo[N][target]