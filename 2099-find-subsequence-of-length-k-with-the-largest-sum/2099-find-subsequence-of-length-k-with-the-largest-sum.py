class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        pq = []
        for i,n in enumerate(nums):
            heapq.heappush(pq,(-n,i))
            
        subsequence = []
        for _ in range(k):
            subsequence.append(heapq.heappop(pq))
            
        subsequence.sort(key=lambda t: t[1])
        return [-n for n,_ in subsequence]