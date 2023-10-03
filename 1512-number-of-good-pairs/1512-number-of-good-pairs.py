class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        pairs = 0
        for n in nums:
            pairs += counts[n]
            counts[n]+=1
        return pairs