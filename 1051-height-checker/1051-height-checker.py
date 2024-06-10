class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        mismatches = 0
        for [a,b] in zip(heights, expected):
            if a != b:
                mismatches += 1
        return mismatches