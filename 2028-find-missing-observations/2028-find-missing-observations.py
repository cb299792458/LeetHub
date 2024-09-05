class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = len(rolls) + n
        missing_total = total * mean - sum(rolls)
        
        avg = missing_total // n
        extra = missing_total % n
        
        if avg<1 or (avg==6 and extra) or avg>6:
            return []
        
        res = [avg] * n
        
        for i in range(extra):
            res[i] += 1
        
        return res