class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = [defaultdict(int) for _ in range(len(nums)+1)]
        # memo[i][total] is the count of ways to reach a total after assigning i symbols
        memo[0][0] = 1
        
        for i in range(len(nums)):
            prev_dict = memo[i]
            num = nums[i]
            for [prev_total, count] in prev_dict.items():
                # for every way to get prev_total, there are that many ways to get to
                # prev_total+num next round, because you can add num to prev_total 
                memo[i+1][prev_total+num] += count 
                memo[i+1][prev_total-num] += count
                
        return memo[-1][target]