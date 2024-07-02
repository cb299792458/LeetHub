class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts1, counts2 = Counter(nums1), Counter(nums2)
        res = []
        for num in counts1.keys():
            res += [num] * min(counts1[num], counts2[num])
        return res