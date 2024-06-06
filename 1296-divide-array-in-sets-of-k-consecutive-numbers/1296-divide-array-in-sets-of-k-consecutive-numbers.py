class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        counts = Counter(nums)
        nums.sort()
        
        for start in nums:
            if not counts[start]:
                continue
            
            for change in range(k):
                if not counts[start+change]:
                    return False
                counts[start+change] -= 1
        
        return True
        