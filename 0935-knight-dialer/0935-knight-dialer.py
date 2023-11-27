class Solution:
    def knightDialer(self, n: int) -> int:
        adjs=[
            [4,6],
            [6,8],
            [7,9],
            [4,8],
            [3,9,0],
            [],
            [1,7,0],
            [2,6],
            [1,3],
            [2,4],
        ]
        mod=10**9+7
        memo=[1]*10
        
        for _ in range(1,n):
            new_memo=[0]*10
            for old in range(10):
                for new in adjs[old]:
                    new_memo[new]+=memo[old]
            memo=new_memo
        
        return sum(memo)%mod