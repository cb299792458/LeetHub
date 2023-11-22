class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        tups = []
        for r,row in enumerate(nums):
            for c,n in enumerate(row):
                tups.append((r+c,c,n))
        
        tups.sort()
        return [n for (_,_,n) in tups]