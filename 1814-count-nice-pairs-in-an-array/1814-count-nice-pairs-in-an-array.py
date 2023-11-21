class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(n):
            return int(str(n)[::-1])
        
        mod = 10**9 + 7
        nums = [n - rev(n) for n in nums]
        counts = Counter(nums)

        return sum([n*(n-1)//2 for n in counts.values()]) % mod