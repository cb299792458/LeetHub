class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2:
            return False
        
        @cache
        def solve(i,diff):
            if i==len(nums):
                if diff:
                    return False
                else:
                    return True
            
            if solve(i+1, diff + nums[i]):
                return True
            if solve(i+1, diff - nums[i]):
                return True
            
            return False
        
        return solve(0,0)