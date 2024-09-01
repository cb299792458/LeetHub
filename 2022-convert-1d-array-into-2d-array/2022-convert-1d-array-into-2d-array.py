class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        res = []
        curr = []
        for num in original:
            curr.append(num)
            if len(curr) == n:
                res.append(curr)
                curr = []
        return res