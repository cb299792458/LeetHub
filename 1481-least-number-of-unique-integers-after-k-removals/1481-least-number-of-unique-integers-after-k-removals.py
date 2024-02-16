class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = Counter(arr)
        counts = list(counts.values())
        counts.sort()
        counts = deque(counts)
        
        while counts and k>=counts[0]:
            k-=counts.popleft()
        return len(counts)