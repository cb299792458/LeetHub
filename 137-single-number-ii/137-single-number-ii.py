class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)
        # print(counts)
        for key,val in counts.items():
            if val==1: return key
            