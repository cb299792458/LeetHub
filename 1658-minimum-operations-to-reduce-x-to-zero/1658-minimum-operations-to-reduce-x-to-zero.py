class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total_sum = sum(nums)
        target = total_sum - x
        n = len(nums)
        l = -1
        curr = 0
        count = float('inf')

        for r in range(n):
            curr += nums[r]

            while curr > target and l < r:
                l += 1
                curr -= nums[l]

            if curr == target:
                count = min(count, n - (r - l))

        return count if count != float('inf') else -1
