class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        score = 0
        
        for _ in range(k):
            most = -heapq.heappop(nums)
            score += most
            heapq.heappush(nums, -((most+2)//3))
        
        return score