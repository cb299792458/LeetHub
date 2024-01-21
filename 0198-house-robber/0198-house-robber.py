class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [nums[0], max(nums[:2])]
        
        for i in range(2, len(nums)):
            memo.append(max(memo[-1],nums[i]+memo[-2]))
        
        return memo[-1]