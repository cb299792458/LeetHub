class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        most = max(candies)
        res = []
        for candy in candies:
            res.append(candy+extraCandies>=most)
        return res