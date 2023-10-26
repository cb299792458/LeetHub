class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        trees = {}
        
        for n in arr:
            trees[n]=1
            for m in arr:
                if m>=n: break
                if not n%m and n//m in arr:
                    trees[n] += (trees[m]*trees[n/m])
        
        return sum(trees.values()) % (10**9+7)