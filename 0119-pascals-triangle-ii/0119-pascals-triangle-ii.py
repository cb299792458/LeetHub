class Solution:
    def getRow(self, numRows: int) -> List[int]:
        prev = [1]
        for _ in range(numRows):
            newRow = []
            for i in range(len(prev)-1):
                newRow.append(prev[i]+prev[i+1])
            prev = [1]+newRow+[1]
        return prev
        