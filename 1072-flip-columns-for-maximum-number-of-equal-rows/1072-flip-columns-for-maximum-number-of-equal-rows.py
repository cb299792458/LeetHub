class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        counts = defaultdict(int)
        MAX = 2**len(matrix[0]) - 1
        
        for row in matrix:
            key = 0
            for n in row:
                key *= 2
                key += n
            key = min(key, MAX - key)
            counts[key] += 1
        
        return max(counts.values())