class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusters = set()
        trusted = [None]
        
        for i in range(1,n+1):
            trusted.append(set())
            
        for truster,trustee in trust:
            trusters.update([truster])
            trusted[trustee].update([truster])
            
        for person in range(1,n+1):
            print(person, person in trusters, trusted[person])
            if person not in trusters and len(trusted[person]) == n-1:
                return person
        
        return -1