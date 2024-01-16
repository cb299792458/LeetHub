class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        
        while l<=r:
            m = (l+r)//2
            mid = nums[m]
            
            if target==mid:
                return m
            elif target<mid:
                r = m - 1
            else:
                l = m + 1
        
        return -1