class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max([m for m in left] + [n-m for m in right])