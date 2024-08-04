class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarray_sums = []
        N = len(nums)
        for i in range(N):
            for j in range(i+1,N+1):
                subarray_sums.append(sum(nums[i:j]))
        
        subarray_sums.sort()
        return sum(subarray_sums[left-1:right]) % (10**9 + 7)