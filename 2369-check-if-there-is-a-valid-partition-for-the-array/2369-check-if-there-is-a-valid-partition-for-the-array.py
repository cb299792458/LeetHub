class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [False]*len(nums)
        dp[1]=nums[0]==nums[1]
        if len(nums)==2: return dp[1]
        dp[2] = nums[0]==nums[1]==nums[2] or nums[0]+2==nums[1]+1==nums[2]
        
        for i in range(3,len(nums)):
            if nums[i]==nums[i-1] and dp[i-2]: dp[i]=True
            if nums[i]==nums[i-1]==nums[i-2] and dp[i-3]: dp[i]=True
            if nums[i]==nums[i-1]+1==nums[i-2]+2 and dp[i-3]: dp[i]=True
        return dp[-1]