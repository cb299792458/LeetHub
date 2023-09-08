class Solution:
    def getRow(self, numRows: int) -> List[int]:
        triangle = [[1]]
        for _ in range(numRows):
            newRow = []
            prev = triangle[-1]
            for i in range(len(prev)-1):
                newRow.append(prev[i]+prev[i+1])
            triangle.append([1]+newRow+[1])
        return triangle[-1]
        