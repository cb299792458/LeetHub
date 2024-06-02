class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2:
            return False
        
        @cache
        def solve(i,total):
            if i==len(nums):
                if total == s//2:
                    return True
                else:
                    return False
            
            if solve(i+1, total + nums[i]):
                return True
            if solve(i+1, total):
                return True
            
            return False
        
        return solve(0,0)