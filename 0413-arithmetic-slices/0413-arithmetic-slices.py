class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = streak = 0
        
        for i,num in enumerate(nums):
            if i<2:
                continue
            if num-nums[i-1] == nums[i-1]-nums[i-2]:
                streak += 1
                count += streak
            else:
                streak = 0
        
        return count