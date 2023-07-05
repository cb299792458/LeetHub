class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l,r,res=0,-1,0
        has_zero=False
        while r<len(nums)-1:
            if has_zero and nums[r+1]==0:
                if nums[l]==0: has_zero=False
                l+=1
            else:
                r+=1
                if nums[r]==0: has_zero=True
            
            res=max(res, r-l)
            
        return res