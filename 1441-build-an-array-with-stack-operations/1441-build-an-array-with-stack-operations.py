class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        
        curr = 1
        for num in target:
            while curr!=num:
                operations.append('Push')
                operations.append('Pop')
                curr+=1
            operations.append('Push')
            curr+=1
        return operations