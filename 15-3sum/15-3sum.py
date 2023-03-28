import numpy as np
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        nums.sort()
        for i in range(len(nums)):
            first = nums[i] #-4
            j = i + 1 #-1
            k = len(nums) - 1 #2
            if(i > 0 and nums[i] == nums[i - 1]):
                continue
            while(j < k):
                if(nums[i] + nums[j] + nums[k] == 0):
                    arr.append([nums[i],nums[j],nums[k]])
                    
                if(nums[i] + nums[j] + nums[k] > 0):
                    k -= 1
                else:
                    j += 1
        res = np.unique(arr, axis=0)
        return res  