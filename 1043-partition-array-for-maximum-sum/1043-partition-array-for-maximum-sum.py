class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)
        memo = [0] * (N+1)
        
        for j in range(N-1, -1, -1):
            for i in range(max(0, j-k+1), j+1):  # Fix the range
                repeats = j - i + 1
                max_val = max(arr[i:j+1])  # Use the correct range
                memo[i] = max(memo[i], (repeats * max_val) + memo[j+1])
        return memo[0]
