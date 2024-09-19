class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        row = []
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                row = matrix[m]
                break
            elif matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1
        
        l, r = 0, len(row) - 1
        while l <= r:
            m = (l + r) // 2
            if row[m] == target:
                return True
            elif row[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False
