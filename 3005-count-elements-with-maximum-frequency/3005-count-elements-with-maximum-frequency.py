class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = list(Counter(nums).values())
        counts.sort()
        return counts[-1] * len([c for c in counts if c==counts[-1]])
        