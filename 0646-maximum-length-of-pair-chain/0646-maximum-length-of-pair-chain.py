class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n=len(pairs)
        
        memo=[1]*n
        
        for i in range(1,n):
            for j in range(0,i):
                if pairs[j][1]<pairs[i][0]:
                    memo[i] = max(memo[i],memo[j]+1)
        return max(memo)
            