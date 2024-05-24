class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curr = 0
        counts = Counter()
        counts[0] = 1
        
        for num in nums:
            curr += num
            res += counts[curr-k]

            counts[curr] += 1
            
        return res