class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res=[set(nums1),set(nums2)]
        for num in nums1:
            res[1].discard(num)
        for num in nums2:
            res[0].discard(num)
        return [list(s) for s in res]