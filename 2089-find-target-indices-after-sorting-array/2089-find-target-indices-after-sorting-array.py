class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        indices = []
        for i in range(len(nums)):
            if target==nums[i]:
                indices.append(i)
        return indices