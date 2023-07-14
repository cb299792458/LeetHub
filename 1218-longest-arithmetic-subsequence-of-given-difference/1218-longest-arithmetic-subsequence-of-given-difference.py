class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        seen=defaultdict(int)
        
        for num in arr:
            seen[num+difference] = seen[num]+1
            
        return max(seen.values())