class Solution:
    def getRow(self, numRows: int) -> List[int]:
        # copy pasted from Pascal's Triangle I
        # not optimized, could save space by only keeping last row
        triangle = [[1]]
        for _ in range(numRows):
            newRow = []
            prev = triangle[-1]
            for i in range(len(prev)-1):
                newRow.append(prev[i]+prev[i+1])
            triangle.append([1]+newRow+[1])
        return triangle[-1]
        