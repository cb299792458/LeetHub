class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for _ in range(numRows-1):
            newRow = []
            prev = triangle[-1]
            for i in range(len(prev)-1):
                newRow.append(prev[i]+prev[i+1])
            triangle.append([1]+newRow+[1])
        return triangle