class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        ops = 0
        for count in counts.values():
            if count==1:
                return -1
            ops += (count+2)//3
        return ops