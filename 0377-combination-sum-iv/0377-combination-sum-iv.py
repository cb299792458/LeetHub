class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = [0] * (target+1)
        memo[0] = 1
        
        for i in range(target+1):
            for num in nums:
                if i+num<=target:
                    memo[i+num]+=memo[i]
        
        return memo[target]