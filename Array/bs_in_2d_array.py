class Solution:

    def searchMatrix(self, matrix, target) -> bool:
        start = 0
        end = len(matrix) * len(matrix[0]) - 1
        m = len(matrix)
        n = len(matrix[0])

        if matrix[0][0] == target:
            return True
        while start <= end:
            mid = (start + end) // 2

            row = mid // n

            column = mid % n

            if matrix[row][column] == target:
                return True
            if matrix[row][column] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False
