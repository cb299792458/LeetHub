class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res=alt=0
        
        for change in gain:
            alt+=change
            res=max(res,alt)
        
        return res