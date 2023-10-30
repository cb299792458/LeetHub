class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        @lru_cache
        def bitCount(n):
            if n==0: return 0
            return n%2 + bitCount(n//2)
        
        arr.sort(key=lambda n: (bitCount(n), n))
        return arr