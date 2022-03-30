class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_idx = bisect.bisect_left(matrix, target, key=lambda x: x[0])
        if row_idx != len(matrix) and matrix[row_idx][0] == target:
            return True
        row = matrix[row_idx - 1]
        target_idx = bisect.bisect_left(row, target)
        return target_idx != len(row) and row[target_idx] == target


# Runtime: 72 ms, faster than 34.08% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 14.4 MB, less than 46.15% of Python3 online submissions for Search a 2D Matrix.
