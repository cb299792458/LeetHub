class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)
        
        @cache
        def dp(i):
            if i==N:
                return 0
            
            largest = 0
            result = 0
            for j in range(k):
                if i + j < N:
                    largest = max(largest, arr[i+j])
                    result = max(result, largest*(j+1) + dp(i+j+1))
            return result
        
        return dp(0)