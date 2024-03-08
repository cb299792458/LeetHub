class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = list(Counter(nums).values())
        most = max(counts)
        return most * len([c for c in counts if c==most])
        