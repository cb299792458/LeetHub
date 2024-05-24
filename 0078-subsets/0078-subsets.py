class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        res = []
        for subarray in self.subsets(nums[1:]):
            res.append(subarray)
            res.append(subarray+[nums[0]])
        
        return res