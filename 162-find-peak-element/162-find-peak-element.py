class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        
        # single element is a peak
        if len(nums)==1: return 0
        
        
        while left<right:
            
            
            # check edges
            if nums[left]>nums[left+1]: return left
            if nums[right]>nums[right-1]: return right
            
            
            mid=(left+right)//2
            
            if nums[mid-1] < nums[mid] > nums[mid+1]: return mid
            
            elif nums[mid-1]>nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
                
        
        
        """
        [1,2,1,3,5,6,4]
         0 1 2 3 4 5 6
         L     M     R
        
        [3,4,3,2,1]
         0 1 2 3 4
         L   M   R
         L R
                 
                 
        """