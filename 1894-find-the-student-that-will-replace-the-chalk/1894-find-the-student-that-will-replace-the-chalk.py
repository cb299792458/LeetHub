class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total=sum(chalk)
        k %= total
        for i,n in enumerate(chalk):
            if k<n:
                return i
            else:
                k -= n