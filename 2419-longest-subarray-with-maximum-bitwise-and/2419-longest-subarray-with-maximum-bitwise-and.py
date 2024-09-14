class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        big = max(nums)
        res = 1
        
        curr = 0
        
        for n in nums:
            if n==big:
                curr += 1
                res = max(curr,res)
            else:
                curr = 0
        return res