class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ops = 0
        
        for i,num in enumerate(nums):
            if i<len(nums)-1 and num>nums[i+1]:
                ops += i+1
        return ops