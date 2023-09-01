class Solution:
    def countBits(self, n: int) -> List[int]:
        memo=[0]
        for i in range(1,n+1):
            memo.append(memo[i//2] + i%2)
        return memo