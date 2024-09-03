class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k%=sum(chalk)
        for i,n in enumerate(chalk):
            if k<n:
                return i
            else:
                k -= n