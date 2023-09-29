class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        dec=True
        inc=True
        prev = nums[0]
        for i in range(1,len(nums)):
            if nums[i]>prev:
                dec=False
            elif nums[i]<prev:
                inc=False
            prev=nums[i]
        return dec or inc