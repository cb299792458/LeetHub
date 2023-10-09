class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def get_first():
            l,r = 0,len(nums)-1
            ans = -1
            while l<=r:
                m = l + (r-l)//2
                if nums[m]>target:
                    r=m-1
                elif nums[m]<target:
                    l=m+1
                else:
                    ans=m
                    r=m-1
            return ans
        
        def get_last():
            l,r = 0,len(nums)-1
            ans=-1
            while l<=r:
                m = l + (r-l)//2
                if nums[m]<target:
                    l=m+1
                elif nums[m]>target:
                    r=m-1
                else:
                    ans=m
                    l=m+1
            return ans
        
        return [get_first(),get_last()]