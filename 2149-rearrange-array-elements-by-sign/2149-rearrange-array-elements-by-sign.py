class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [n for n in nums if n>0]
        neg = [n for n in nums if n<0]
        
        res = []
        for [p,n] in zip(pos,neg):
            res.append(p)
            res.append(n)
        return res