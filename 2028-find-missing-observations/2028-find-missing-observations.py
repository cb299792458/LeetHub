class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = len(rolls) + n
        missing_total = total * mean - sum(rolls)
        
        if missing_total>6*n or missing_total<n:
            return []
        
        avg = missing_total // n
        extra = missing_total % n
        
        return [avg + int(i<extra) for i in range(n)]