class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        mps = 0
        l,r = 0,len(nums)-1
        while l<r:
            mps=max(nums[l]+nums[r],mps)
            l+=1
            r-=1
        return mps