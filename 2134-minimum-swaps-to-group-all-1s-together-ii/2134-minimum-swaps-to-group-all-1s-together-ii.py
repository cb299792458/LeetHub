class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        ones = sum(e==1 for e in nums)
        zeros = sum(e==0 for e in nums[:ones])
        
        nums += nums
        swaps = zeros
        
        for i in range(N):
            j = i+ones
            if nums[i] == 0:
                zeros -= 1
            if nums[j] == 0:
                zeros += 1
            swaps = min(swaps, zeros)

            
        return swaps