class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(n):
            return int(str(n)[::-1])
        
        mod = 10**9 + 7
        nums = [n - rev(n) for n in nums]
        counts = Counter()
        pairs = 0
        
        for n in nums:
            pairs += counts[n]
            counts[n] += 1
            
        return pairs % mod