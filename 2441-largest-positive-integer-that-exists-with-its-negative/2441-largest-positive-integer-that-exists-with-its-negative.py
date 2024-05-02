class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        best = -1
        num_set = set(nums)
        for n in nums:
            if -n in num_set:
                best = max(best,n)
        return best